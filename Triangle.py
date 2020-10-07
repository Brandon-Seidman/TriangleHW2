# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def _classify_triangle(_a,_b,_c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """
    _in_a = isinstance(_a,int)
    _in_b = isinstance(_b,int)
    _in_c = isinstance(_c,int)
    _ov_th = _a > 200 or _b > 200 or _c > 200
    _lt_z = _a <= 0 or _b <= 0 or _c <= 0
    # require that the input values be >= 0 and <= 200

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(_in_a and _in_b and _in_c) or _ov_th or _lt_z:
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (_a >= (_b + _c)) or (_b >= (_a + _c)) or (_c >= (_a + _b)):
        return 'NotATriangle'

    _a_pow = pow(_a,2)
    _b_pow = pow(_b,2)
    _c_pow = pow(_c,2)

    # now we know that we have a valid triangle
    if _a == _b and _c == _a and _c == _b:
        return 'Equilateral'
    if _a_pow + _b_pow == _c_pow or _a_pow + _c_pow == _b_pow or _c_pow + _b_pow == _a_pow:
        return 'Right'
    if (_a != _b) and  (_b != _c) and (_a != _c):
        return 'Scalene'
    return 'Isoceles'
