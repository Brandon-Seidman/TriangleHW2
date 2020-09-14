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

    def testNotATriangle1(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1,2,3 should be NotATriangle') #Normal Test

    def testNotATriangle2(self):
        self.assertEqual(classifyTriangle(2,3,1),'NotATriangle','2,3,1 should be NotATriangle') #Tests different positions

    def testNotATriangle3(self):
        self.assertNotEqual(classifyTriangle(2,2,3),'NotATriangle','Should not be NotATriangle') #Tests an actual triangle

    def testNotATriangle4(self):
        self.assertNotEqual(classifyTriangle(2,3,2),'NotATriangle','Should not be NotATriangle') #Tests an actual triangle in different positions

    def testNotATriangle5(self):
        self.assertEqual(classifyTriangle(5*2,6/3,89/1),'NotATriangle','Should be NotATriangle') #Tests with equations



    def testEquilateralTriangle1(self):
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral','Should be Equilateral') #Normal Test

    def testEquilateralTriangle2(self):
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral','Should be Equilateral') #Tests different numbers

    def testEquilateralTriangle3(self):
        self.assertNotEqual(classifyTriangle(3,3,2),'Equilateral','Should not be Equilateral') #Tests a non equilateral triangle (2 similar sides)

    def testEquilateralTriangle4(self):
        self.assertNotEqual(classifyTriangle(3,2,3),'Equilateral','Should not be Equilateral') #Tests a non equilateral triangle (2 similar sides different positions)

    def testEquilateralTriangle5(self):
        self.assertNotEqual(classifyTriangle(2,3,3),'Equilateral','Should not be Equilateral') #Tests a non equilateral triangle (2 similar sides different positions)

    def testEquilateralTriangle6(self):
        self.assertNotEqual(classifyTriangle(5,2,3),'Equilateral','Should not be Equilateral') #Tests no similar sides

    def testEquilateralTriangle7(self):
        self.assertEqual(classifyTriangle(12,6*2,3*4),'Equilateral','Should be Equilateral') #Tests equations



    # def testRightTriangles1(self):
    #     self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle') #Normal Test
    #
    # def testRightTriangles2(self):
    #     self.assertEqual(classifyTriangle(4,5,3),'Right','4,5,3 is a Right triangle') #Tests different positions
    #
    # def testRightTriangles3(self):
    #     self.assertNotEqual(classifyTriangle(6,4,4),'Right','6,4,4 should not be Right') #Tests a non right triangle
    #
    # def testRightTriangles4(self):
    #     self.assertNotEqual(classifyTriangle(4,4,6),'Right','4,4,6 should not be Right') #Tests a non right triangle in different positions
    #
    # def testRightTriangles5(self):
    #     self.assertEqual(classifyTriangle(5*17,13*17,12*17),'Right','Should be Right') #Tests with equations

    # def testScaleneTriangle1(self):
    #
    # def testIsocelesTriangle1(self):


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
