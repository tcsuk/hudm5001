#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 21:43:09 2023

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
# Task: Verify method appendGrade() works properly (it adds a grade) 

import unittest

tc = unittest.TestCase()

# append a grade to each student
s1.appendGrade(82)
s2.appendGrade(80)

print("after appending a grade to each:")
print(s1.grades)
print(s2.grades)

# Test: using assertEqual() method, comparing expected to actual data
expected1 = [82]
expected2 = [90,95,80]

print(tc.assertEqual(s1.grades, expected1))
print(tc.assertEqual(s2.grades, expected2))

# Both tests pass!