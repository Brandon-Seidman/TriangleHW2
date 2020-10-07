# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from _triangle import _classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

_NAT = 'NotATriangle'
_SB_NAT = 'Should be NotATriangle'
_SB_NNAT = 'Should not be NotATriangle'
_EQ = 'Equilateral'
_SB_EQ = 'Should be Equilateral'
_SB_NEQ = 'Should not be Equilateral'
_R = 'Right'
_SB_R = 'Should be Right'
_SB_NR = 'Should not be Right'
_S = 'Scalene'
_SB_S = 'Should be Scalene'
_SB_NS = 'Should not be Scalene'
_I = 'Isoceles'
_SB_I = 'Should be Isoceles'
_SB_NI = 'Should not be Isoceles'

class _TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def test_not_a_triangle_1(self):
        '''NaT1'''
        self.assertEqual(_classify_triangle(1,2,3),_NAT,_SB_NAT)
        #Normal Test

    def test_not_a_triangle_2(self):
        '''NaT2'''
        self.assertEqual(_classify_triangle(2,3,1),_NAT,_SB_NAT)
        #Tests different positions

    def test_not_a_triangle_3(self):
        '''NaT3'''
        self.assertNotEqual(_classify_triangle(2,2,3),_NAT,_SB_NNAT)
        #Tests an actual triangle

    def test_not_a_triangle_4(self):
        '''NaT4'''
        self.assertNotEqual(_classify_triangle(2,3,2),_NAT,_SB_NNAT)
    #Tests an actual triangle in different positions

    def test_not_a_triangle_5(self):
        '''NaT5'''
        self.assertEqual(_classify_triangle(10,2,89),_NAT,_SB_NAT)
        #Tests with equations



    def test_equilateral_triangle_1(self):
        '''E1'''
        self.assertEqual(_classify_triangle(3,3,3),_EQ,_SB_EQ)
        #Normal Test

    def test_equilateral_triangle_2(self):
        '''E2'''
        self.assertEqual(_classify_triangle(5,5,5),_EQ,_SB_EQ)
        #Tests different numbers

    def test_equilateral_triangle_3(self):
        '''E3'''
        self.assertNotEqual(_classify_triangle(3,3,2),_EQ,_SB_NEQ)
        #Tests a non equilateral triangle (2 similar sides)

    def test_equilateral_triangle_4(self):
        '''E4'''
        self.assertNotEqual(_classify_triangle(3,2,3),_EQ,_SB_NEQ)
        #Tests a non equilateral triangle (2 similar sides different positions)

    def test_equilateral_triangle_5(self):
        '''E5'''
        self.assertNotEqual(_classify_triangle(2,3,3),_EQ,_SB_NEQ)
        #Tests a non equilateral triangle (2 similar sides different positions)

    def test_equilateral_triangle_6(self):
        '''E6'''
        self.assertNotEqual(_classify_triangle(5,2,3),_EQ,_SB_NEQ)
        #Tests no similar sides

    def test_equilateral_triangle_7(self):
        '''E7'''
        self.assertEqual(_classify_triangle(12,6*2,3*4),_EQ,_SB_EQ)
        #Tests equations



    def test_right_triangle_1(self):
        '''R1'''
        self.assertEqual(_classify_triangle(3,4,5),_R,_SB_R)
        #Normal Test

    def test_right_triangle_2(self):
        '''R2'''
        self.assertEqual(_classify_triangle(4,5,3),_R,_SB_R)
        #Tests different positions

    def test_right_triangle_3(self):
        '''R3'''
        self.assertNotEqual(_classify_triangle(6,4,4),_R,_SB_NR)
        #Tests a non right triangle

    def test_right_triangle_4(self):
        '''R4'''
        self.assertNotEqual(_classify_triangle(4,4,6),_R,_SB_NR)
        #Tests a non right triangle in different positions

    def test_right_triangle_5(self):
        '''R5'''
        self.assertEqual(_classify_triangle(5*7,13*7,12*7),_R,_SB_R)
        #Tests with equations



    def test_scalene_triangle_1(self):
        '''S1'''
        self.assertEqual(_classify_triangle(4,3,2),_S,_SB_S)
        #Normal Test

    def test_scalene_triangle_2(self):
        '''S2'''
        self.assertEqual(_classify_triangle(2,4,5),_S,_SB_S)
        #Tests different numbers

    def test_scalene_triangle_3(self):
        '''S3'''
        self.assertNotEqual(_classify_triangle(3,3,2),_S,_SB_NS)
        #Tests a non scalene triangle

    def test_scalene_triangle_4(self):
        '''S4'''
        self.assertNotEqual(_classify_triangle(3,2,3),_S,_SB_NS)
        #Tests a non scalene triangle (different positions)

    def test_scalene_triangle_5(self):
        '''S5'''
        self.assertNotEqual(_classify_triangle(2,3,3),_S,_SB_NS)
        #Tests a non scalene triangle (different positions)

    def test_scalene_triangle_6(self):
        '''S6'''
        self.assertNotEqual(_classify_triangle(3,3,3),_S,_SB_NS)
        #Tests a non scalene triangle (all three same)

    def test_scalene_triangle_7(self):
        '''S7'''
        self.assertEqual(_classify_triangle(4*6,3*6,2*6),_S,_SB_S)
        #Tests with equations



    def test_isoceles_triangle_1(self):
        '''I1'''
        self.assertEqual(_classify_triangle(4,4,2),_I,_SB_I)
        #Normal Test

    def test_isoceles_triangle_2(self):
        '''I2'''
        self.assertEqual(_classify_triangle(2,5,5),_I,_SB_I)
        #Tests different positions

    def test_isoceles_triangle_3(self):
        '''I3'''
        self.assertEqual(_classify_triangle(5,2,5),_I,_SB_I)
        #Tests different positions

    def test_isoceles_triangle_4(self):
        '''I4'''
        self.assertNotEqual(_classify_triangle(3,5,2),_I,_SB_NI)
        #Tests none the same

    def test_isoceles_triangle_5(self):
        '''I5'''
        self.assertNotEqual(_classify_triangle(2,2,2),_I,_SB_NI)
        #Tests all the same

    def test_isoceles_triangle_6(self):
        '''I6'''
        self.assertEqual(_classify_triangle(4*1,4*1,2*1),_I,_SB_I)
        #Tests with equations


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
