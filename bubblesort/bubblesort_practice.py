#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:49:16 2020

@author: stanley-yu
"""
import random 

randomlist = [] 

for i in range(0,5):
    n = random.randint(1,30)
    randomlist.append(n)

def bubblesort(arr): 
    n = len(arr) 
    for i in range(n): 
        print(arr) 
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                copy = arr[j] 
                arr[j] = arr[j+1]
                arr[j+1] = copy
    print(arr) 
    return arr
                
                

bubblesort(randomlist)




