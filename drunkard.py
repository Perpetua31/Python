#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:43:40 2024

@author: Perpetua Senatus

The Drunkard's walk

Imagine a city that consists of a grid of streets. 
Now imagine a drunkard that starts at any given intersection of such a grid and randomly picks
one of four directions to go and then stumbles to the next intersection. 
There, they randomly choose one of four directions to travel, stumble to the next intersection, and so on.  
After many such steps, where is the drunkard? 
Intuition may tell us that he shouldn’t be far since the random direction choices would ultimately cancel each other out.
Intuition would be wrong. 

We can represent intersections on this grid using Cartesian coordinates (x,y). 
Write a program in Python that begins with the drunkard at the origin of such a grid (0,0), 
then use a loop to have the drunkard move through 100 intersections. Print the ending location and calculate its distance from (0,0).

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


