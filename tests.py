# doctest vs unittest
# https://stackoverflow.com/questions/361675/python-doctest-vs-unittest

import unittest
# https://realpython.com/python-testing/#writing-your-first-test
import random

# myArtNet.py
from myArtNet import ArtNetNode

class TestNodeMethods(unittest.TestCase):
    def setUp(self):
        self.node = ArtNetNode("0.0.0.0", 5000, testing=True)
    
    def testSmallStringb2l(self):
        b = b'\x00\xff'
        self.assertEqual(self.node._bin2list(b), [0,255])
    
    def testLargeStringb2l(self):
        b = b'Art-Net\x00\x00P\x00\x0e[\x00\x00\x00\x000\xff\x00'
        res = self.node._bin2list(b)
        self.assertEqual(res,[65, 114, 116, 45, 78, 101, 116, 0, 0, 80, 0, 14, 91, 0, 0, 0, 0, 48, 255, 0])
        # list equality is order dependant, so if pass assertEqual here then can confirm order not been changed
    
    # doesn't need to be tested as I'm using built in bytes() function
    # wrote the test before implementing the method so may as well keep it
    def testl2b(self):
        l = [65, 114, 116, 45, 78, 101, 116, 0, 0, 80, 0, 14, 91, 0, 0, 0, 0, 48, 255, 0]
        res = self.node._list2bin(l)
        self.assertEqual(res, b'Art-Net\x00\x00P\x00\x0e[\x00\x00\x00\x000\xff\x00')


# webUI.py
# TODO: need to decide on how errors will be returned to user and for testing -> woo for TDD
# TODO: test updateconf, need to add a load of data validation there
from webUI import updateConf
from shutil import copyfile

class testWebUIFuncs(unittest.TestCase):
    # setUp() is run before every test
    def setUp(self):
        #copyfile("config/conf.ini.default", "config/conf.ini.test")
        # Hmm but all the code looks at conf.ini
        copyfile("config/conf.ini", "config/confLive.ini.copy")
        copyfile("config/conf.ini.default", "config/conf.ini")
        self.testForm = {
            "inputName" : "",
            "address" : "",
            "universe": "",
            "num" : "",
        }
        # v v v v v 
        # TODO: don't test with the conf.ini file, have a test conf file that's edited and changed etc
        # ^ ^ ^ ^ ^ 
        # I know how I'm doing it rn is bad but I want to focus on writing tests and not restructing my code yet
        # this is in a branch, I will sort this before I merge to master
    # tearDown is run after every test
    def tearDown(self):
        copyfile("config/confLive.ini.copy", "config/conf.ini")

    # Test default conf file is updated correctly, 
    # trying different conf options, and number of options updated in one go
    def testUpdateConf(self):
        self.testForm["inputName"] = "Test Name"
        self.testForm["address"]   = "100"
        self.testForm["universe"]  = "2"
        self.testForm["num"]       = "50"

        updateConf(self.testForm)
        # TODO: uhh, need to read the file and see if the file reads as expected
        # can do a normal read rather than using the configparser library methinks
        

    # Test that if trying to update a non-supported config option fails
    def testUpdateConfFails(self):
        self.skipTest("Not set up")
        pass
    
    def testUpdateConfValidation(self):
        self.skipTest("Not set up")
        pass

    def test512Limit1(self):
        self.skipTest("Not set up")
    


# artnetLEDController.py
# as it currently is, there doesn't seem to be anything to test in that I think?





if __name__ == "__main__":
    print(">>> NOTE <<<")
    #print("Running tests may revert config to default")
    print("confLive.ini.copy will be created and overwritten with a copy of the config file.\nIf you have a file with this name, do not continue.")

    inp = input("Enter y to continue:  ")
    if (inp == 'y'):
        try:
            unittest.main()
        except KeyboardInterrupt:
            pass
    
    print("Quitting tests")