#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:34:38 2024

@author: Perpetua Senatus


The sum of 100 random numbers chosen between 1 and 10 (inclusive)

"""

import random

total_random = 0

for i in range(100):
    rn = random.randint(1, 10) 
    total_random = total_random + rn  


print("Sum of 100 random numbers:", total_random)
