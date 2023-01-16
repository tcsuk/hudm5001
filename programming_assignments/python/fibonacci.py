# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 21:51:54 2023

@author: youmisuk
"""

def fibonacci_robust(n):
    
    if (not isinstance(n, int)) or (n < 0):
        return -1
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_robust(n-1) + fibonacci_robust(n-2)
    
print('FIBONACCI SCRIPT')
print('fibonacci_robust(6)=',fibonacci_robust(6))
