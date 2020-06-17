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

def bubblesort(array): 
    for i in range(len(array)): 
        n = len(array) 
        print(array)
        for j in range(n-1): 
            if array[j] > array[j+1]:
                copy = array[j] 
                array[j] = array[j+1]
                array[j+1] = copy
    return array


bubblesort(randomlist)