#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:43:40 2024

@author: Perpetua Senatus

The Drunkard's walk

"""

import random
import math

x = 0
y = 0

for i in range(100):
    position = random.randint(1, 4)  
    print(f"The Drunkard is at: ({x}, {y})")
    if position == 1:  # north
        y += 1  
    elif position == 2:  # south
        y -= 1
    elif position == 3:  # west
        x -= 1
    elif position == 4:  # east
        x += 1


# Formula to calculate the distance from the origin (0,0)
distance = math.sqrt(x**2 + y**2)

print(f"The Drunkard's ending location after 100 intersections is: ({x}, {y})")
print(f"The distance from the origin is: {distance:.2f}")


