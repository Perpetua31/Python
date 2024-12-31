#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:35:38 2024

@author: Perpetua Senatus


1) A function that computes the Hamming distance between two strings

2) A function that determines if any string of any length is a palindrome
by returning  a boolean. 

"""

# User input for two strings
s1 = str(input("s1 = "))
s2 = str(input("s2 = "))

# Ensure both strings are the same length
while len(s1) != len(s2):
    print("s2 is not the same length as s1, try again!")
    s1 = str(input("s1 = "))
    s2 = str(input("s2 = "))

# Function to get hamming distance
def hamming_distance(s1, s2):
    # Initialize the count
    subs = 0
    
    # Loop to check whether the characters at 
    # each position in both strings are identical
    # if not increment subs
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            subs = subs + 1
            
    #return total subs      
    return subs

# Call the function 
result = hamming_distance(s1, s2)

# Display the result
print("Hamming distance:", result, "\n")



# Function to check if a string is a palindrome
def is_palindrome(s3):
    
    # Convert the string to lowercase
    # to make it case insensitive 
    s3 = s3.lower()
    
    # Check if string is a palindrome
    return s3 == s3[::-1]

print(is_palindrome("hanNah")) 
