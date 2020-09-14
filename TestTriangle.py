# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangles(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle') #Normal Test
        self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle') #Tests different positions
        self.assertNotEqual(classifyTriangle(6,4,4),'Right','Should not be Right') #Tests a non right triangle
        self.assertNotEqual(classifyTriangle(4,4,6),'Right','Should not be Right') #Tests a non right triangle in different positions
        self.assertEqual(classifyTriangle(5*17,13*17,12*17),'Right','Should be Right') #Tests equations instead of numbers

    # def testEquilateralTriangles(self):
    #
    # def testScaleneTriangles(self):
    #
    # def testIsocelesTriangles(self):
    #
    # def testNotATriangles(self):


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
