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
from webUI import updateConf, validateConf
from shutil import copyfile

class testWebUIFuncs(unittest.TestCase):
    # setUp() is run before every test
    def setUp(self):
        #copyfile("config/conf.ini.default", "config/conf.ini.test")
        # Hmm but all the code looks at conf.ini
        copyfile("config/conf.ini", "config/confLive.ini.copy")
        copyfile("config/conf.ini.default", "config/conf.ini")
        self.testForm = {
            "inputName" : "Test Name",
            "address" : "100",
            "universe": "2",
            "num" : "50",
        }
        self.testForm2 = {
            "inputName" : "Test Name2",
            "address" : "1",
            "universe": "1",
            "num" : "1",
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
        updateConf(self.testForm)

        f = open("config/conf.ini")
        lines = f.readlines()
        f.close()
        # TODO: Look in to a better way to do this
        expected = [
            "[artnetNode]\n",
            "name = Test Name\n",
            "numled = 50\n",
            "startaddr = 100\n",
            "dmxuniverse = 2\n",
            "\n"
        ]
        self.assertEqual(lines, expected)
        
    def testValidateConfPass(self):
        err = validateConf(self.testForm)
        self.assertEqual(err,[])
    
    # Tests different cases of address to see if it errors or not
    def testValidateAddressSimple(self):
        testAdresses = {"hi":False, "True":False, "\n":False,
        -1:False,0:False,1:True,100:True,509:True,510:True,511:False,512:False,513:False}
        for case  in testAdresses.keys():
            with self.subTest(msg = "case: "+str(case)):
                self.testForm2["address"] = str(case)
                err = validateConf(self.testForm2)
                if (testAdresses[case]): # ie. expecting to pass/no errors
                    self.assertEqual(err, [])
                else: # ie. expecting at least one error
                    self.assertGreater(len(err), 0)
    
    # Tests different addresses to see if error returned is as expected
    def testValidateAddress(self):
        self.subTest(msg = "Testing not a number")
        expected = ["Address must be a number"]
        self.testForm["address"] = "hi"
        err = validateConf(self.testForm)
        self.assertEqual(err, expected)

        self.subTest(msg = "Testing out of range")
        expected = ["Address must be in range in range 1-512 inclusive"]
        self.testForm["address"] = "0"
        err = validateConf(self.testForm)
        self.assertEqual(err, expected) # code repetition, but I like how I'm organising subtests
        self.testForm["address"] = "-1"
        err = validateConf(self.testForm)
        self.assertEqual(err, expected)
        self.testForm["address"] = "513"
        err = validateConf(self.testForm)
        self.assertEqual(err, expected)

    def testValidateNum(self):
        self.subTest(msg = "Testing success cases")


        self.subTest(msg = "Testing failure cases")
        expected = ["Number of pixels must be an integer"]

        self.subTest(msg = "Testing num pixels fits within address-512")
        self.testForm2["address"] = "1"
        self.testForm2["num"] = 170 # This one will pass
        err = validateConf(self.testForm2)
        self.assertEqual(err, [])
        expected = ["Too many pixels or too high address"]
        self.testForm2["num"] = 171
        err = validateConf(self.testForm2)
        self.assertEqual(err, expected)
        
        self.testForm2["address"] = 501
        self.testForm2["num"] = 4
        err = validateConf(self.testForm2)
        self.assertEqual(err, [])
        self.testForm2["num"] = 5
        self.assertEqual(err, expected)

    


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
            # Do I need to run the tear down methods???
    
    print("Quitting tests")