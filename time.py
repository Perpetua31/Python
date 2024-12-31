#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 23:15:19 2024

@author: Perpetua Senatus

A program that will print the time on a clock

"""

time_now = int(input("Enter the time now in hours: "))

wait_time = int(input("Enter the number of hours to wait: "))

time_clock_off =((time_now + wait_time) % 24)

print("When the alarm goes off, the time on the clock will be: ",time_clock_off)

