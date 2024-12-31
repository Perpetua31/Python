#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 23:16:46 2024

@author: Perpetua Senatus

A program that will compute MPG for a car

"""

num_miles = float(input("Enter the number of miles driven: "))

num_gallons = float(input("Enter the number of gallons used: "))

#Formula to calculate MPG
mpg = num_miles/num_gallons

print(f"The MPG of the car is {mpg:.2f}")
