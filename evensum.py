#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:33:16 2024

@author: Perpetua Senatus

A program that computes the sum of all even numbers between 1 and 100 (inclusive)

"""

total_even = 0


for num in range(1, 101):
    if num % 2 == 0:
        total_even = total_even + num  
     

print("Sum of all even numbers between 1 and 100:", total_even)
     

