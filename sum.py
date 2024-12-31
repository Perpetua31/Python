#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:31:22 2024

@author: Perpetua Senatus 

A program that compute the sum of all numbers between 1 and 100 (inclusive)


"""
total_sum = 0  

for num in range(1, 101):
    total_sum = total_sum + num  
    

print("Sum of all numbers between 1 and 100:", total_sum)
