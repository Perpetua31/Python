#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 23:17:50 2024

@author: Perpetua Senatus

A program that will convert degrees Fahrenheit to degrees Celsius.


"""

deg_fah=float(input('Enter the temperature in Fahrenheit: '))

#Formula to convert Fahrenheit to Celsius
fah_to_cel = 5 / 9 * (deg_fah - 32) 

print(f"{deg_fah} degrees Fahrenheit is equal to {fah_to_cel:.1f} degrees Celsius.")

