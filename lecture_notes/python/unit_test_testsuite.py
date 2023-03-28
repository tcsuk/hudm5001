#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 07:46:22 2023

@author: ys2952
"""

## create a student class; handle cases where grades empty

class Student:
    
    # constructor
    def __init__(self, name, id, grades=None):
        self.name= name
        self.id= id
        
        # set grades to empty list if not provided
        self.grades = [] if grades is None else grades

    # method for appending a grade to the list of grades
    def appendGrade(self, grade):
        self.grades.append(grade)

# create some students
s1 = Student('Jack',123)
s2 = Student('Jane',123,[90,95])

# print their grades
print('s1 grades:', s1.grades)
print('s2 grades:', s2.grades)

# Unit Testing
# To test out your Student class, you will write a test suite of unit tests.
# Write the unit tests below, starting all your function names with “test_”.
# Verify method appendGrade() works properly (it adds a grade) 
# Run your test cases, and ensure all your unit tests pass.

import unittest


class StudentTestSuite(unittest.TestCase):

    # create some students
    a1 = Student('Jack',123)
    a2 = Student('Jane',123,[90,95])

    # append a grade to each student
    a1.appendGrade(82)
    a2.appendGrade(80)

    # test 1 using assertEqual() method
    def test_1_appendGrade(self):  
        expected = [82]
        self.assertEqual(self.a1.grades, expected)
        
    # test 2 using assertEqual() method
    def test_2_appendGrade(self):  
        expected = [90,95,80]
        self.assertEqual(self.a2.grades, expected)        

if __name__ == '__main__':
    unittest.main() 
# Both tests pass!