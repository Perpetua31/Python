#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 23:17:15 2024

@author: Perpetua Senatus

A program that will convert degrees Celsius to degrees Fahrenheit.

"""

deg_cel = float(input("Enter the temperature in Celsius: "))

#Formula to convert Celsius to Fahrenheit
cel_to_fah = deg_cel * (9 / 5) + 32

print(f"{deg_cel} degrees Celsius is equal to {cel_to_fah:.1f} degrees Fahrenheit.")
