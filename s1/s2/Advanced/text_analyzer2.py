# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 20:24:43 2016

@author: jillzhang
"""

Input=raw_input("Enter the word: ")
vowel=['a','e','i','o','u']
output={}

for x in vowel:
    output[x]=Input.count(x)
    
print output