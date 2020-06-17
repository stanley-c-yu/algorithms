#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:06:30 2020

@author: stanley-yu
"""
import unittest;
from bubblesort import bubbleSort; 

class bubbleSortTestCase(unittest.TestCase): 
    """Tests for 'bubblesort.py'."""
    
    def test_pre_sorted(self): 
        """Will bubble sort accept a pre-sorted array without failure?"""
        result = bubbleSort([5,10,15,20,25,30]);
        self.assertEqual(result, [5,10,15,20,25,30]);
        
    def test_reverse_sorted(self):
        """Can bubble sort correctly sort a reverse sorted array?""" 
        result = bubbleSort([150, 83, 23, 12, 10, 6.2, 5]);
        self.assertEqual(result,[5,6.2,10,12,23,83,150]);
        
    def test_mix_sorted(self): 
        """Can bubble sort handle an array with number in mixed order?"""
        result = bubbleSort([3,2,1,4,5]);
        self.assertEqual(result,[1,2,3,4,5]);
        
unittest.main()
        
