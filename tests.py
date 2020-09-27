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
# TODO: test updateconf, need to add a load of data validation there, so maybe use TDD
from webUI import updateConf

class testWebUIFuncs(unittest.TestCase):
    def setUp(self):
        pass
        #TODO: set up test config file

    # Test default conf file is updated correctly, 
    # trying different conf options, and number of options updated in one go
    def testUpdateConf(self):
        self.skipTest("Not set up")
        pass

    # Test that if trying to update a non-supported config option fails
    def testUpdateConfFails(self):
        self.skipTest("Not set up")
        pass
    
    def testUpdateConfValidation(self):
        self.skipTest("Not set up")
        pass
    


# artnetLEDController.py
# as it currently is, there doesn't seem to be anything to test in that I think?





if __name__ == "__main__":
    unittest.main()