#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:24:08 2020

@author: stanley-yu
"""
import time 

def bubbleSort(array): 
    start_time = time.time();
    for i in range(len(array)): 
        n = len(array) - i - 1;
        print(array);
        for j in range(0,n):
            #print(array[j]);
            if array[j] > array[j+1]:
                copy = array[j];
                array[j] = array[j+1];
                array[j+1] = copy;
    stop_time = time.time();
    print("Complete! Approximate time elapsed: ", round(stop_time-start_time,10), "seconds.");
    return array;

# tmp_array = [5,4,3,2,1];

# bubbleSort(tmp_array);