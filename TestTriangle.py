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
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','Should be NotATriangle') #Normal Test

    def testNotATriangle2(self):
        self.assertEqual(classifyTriangle(2,3,1),'NotATriangle','Should be NotATriangle') #Tests different positions

    def testNotATriangle3(self):
        self.assertNotEqual(classifyTriangle(2,2,3),'NotATriangle','Should not be NotATriangle') #Tests an actual triangle

    def testNotATriangle4(self):
        self.assertNotEqual(classifyTriangle(2,3,2),'NotATriangle','Should not be NotATriangle') #Tests an actual triangle in different positions

    def testNotATriangle5(self):
        self.assertEqual(classifyTriangle(10,2,89),'NotATriangle','Should be NotATriangle') #Tests with equations



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



    def testRightTriangle1(self):
        self.assertEqual(classifyTriangle(3,4,5),'Right','Should not be Right') #Normal Test

    def testRightTriangle2(self):
        self.assertEqual(classifyTriangle(4,5,3),'Right','Should not be Right') #Tests different positions

    def testRightTriangle3(self):
        self.assertNotEqual(classifyTriangle(6,4,4),'Right','Should not be Right') #Tests a non right triangle

    def testRightTriangle4(self):
        self.assertNotEqual(classifyTriangle(4,4,6),'Right','Should not be Right') #Tests a non right triangle in different positions

    def testRightTriangle5(self):
        self.assertEqual(classifyTriangle(5*7,13*7,12*7),'Right','Should be Right') #Tests with equations



    def testScaleneTriangle1(self):
        self.assertEqual(classifyTriangle(4,3,2),'Scalene','Should be Scalene') #Normal Test

    def testScaleneTriangle2(self):
        self.assertEqual(classifyTriangle(2,4,5),'Scalene','Should be Scalene') #Tests different numbers

    def testScaleneTriangle3(self):
        self.assertNotEqual(classifyTriangle(3,3,2),'Scalene','Should not be Scalene') #Tests a non scalene triangle

    def testScaleneTriangle4(self):
        self.assertNotEqual(classifyTriangle(3,2,3),'Scalene','Should not be Scalene') #Tests a non scalene triangle (different positions)

    def testScaleneTriangle5(self):
        self.assertNotEqual(classifyTriangle(2,3,3),'Scalene','Should not be Scalene') #Tests a non scalene triangle (different positions)

    def testScaleneTriangle6(self):
        self.assertNotEqual(classifyTriangle(3,3,3),'Scalene','Should not be Scalene') #Tests a non scalene triangle (all three same)

    def testScaleneTriangle7(self):
        self.assertEqual(classifyTriangle(4*6,3*6,2*6),'Scalene','Should be Scalene') #Tests with equations



    def testIsocelesTriangle1(self):
        self.assertEqual(classifyTriangle(4,4,2),'Isoceles','Should be Isoceles') #Normal Test

    def testIsocelesTriangle2(self):
        self.assertEqual(classifyTriangle(2,5,5),'Isoceles','Should be Isoceles') #Tests different positions

    def testIsocelesTriangle3(self):
        self.assertEqual(classifyTriangle(5,2,5),'Isoceles','Should be Isoceles') #Tests different positions

    def testIsocelesTriangle4(self):
        self.assertNotEqual(classifyTriangle(3,5,2),'Isoceles','Should not be Isoceles') #Tests none the same

    def testIsocelesTriangle5(self):
        self.assertNotEqual(classifyTriangle(2,2,2),'Isoceles','Should not be Isoceles') #Tests all the same

    def testIsocelesTriangle6(self):
        self.assertEqual(classifyTriangle(4*1,4*1,2*1),'Isoceles','Should be Isoceles') #Tests with equations


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
