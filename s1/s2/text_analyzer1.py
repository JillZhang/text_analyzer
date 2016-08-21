# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 14:24:21 2016

@author: jillzhang
"""

Input=raw_input("Enter the word: ")
vowel=['a','e','i','o','u']
input_len=len(Input)
counts=0
for x in range(0,input_len):
    if Input[x] in vowel:
        counts+=1
        if counts==1:
            first_vowel=x
if counts>=1:
            print "vowels: ",counts
            print "first vowel :",Input[first_vowel]
else:
    print "there is no vowel in the string"
if first_vowel<input_len:
    print "character immediately after first vowel: ",Input[first_vowel+1]       
else:
    print "the first vowel is last character in the string"