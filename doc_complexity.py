# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 14:25:26 2016

@author: David A. Rynties
"""

import time
from string import punctuation
import collections

file = 'C:\\users\\user\\Desktop\\Medical and Bioinformatics\\677\\alice_in_wonderland.txt'
test_windows = [10, 250, 1000, 3000, 5000]
single_window = 1000

def strip_punctuation(s):
    """remove all punctuation from text"""
    return ''.join(c for c in s if c not in punctuation)

def list_breakdown(text, sliding_window_value):
    """break list into groups equaled to the sliding window value """
    min_value = 0
    max_value = sliding_window_value 
    while max_value <= len(text):
        current_window = text[min_value:max_value]
        frame_complexity = calc_complexity(current_window)
        min_value += 1
        max_value += 1
        total_complexity.append(frame_complexity)

def calc_complexity(list_a): 
    """calculate the complexity of the list"""
    count_values_def = collections.Counter(list_a)
    aspect_complexity= len(count_values_def) / len(list_a)
    return aspect_complexity

#open file

with open(file, 'r') as f: 
    total_complexity = []
    list_complexities = []
    complete_text = strip_punctuation(f.read().replace('—', ' '))  
    clean_text = complete_text.lower().split()
    count_values = collections.Counter(clean_text)

document_complexity = len(count_values) / len(clean_text)

list_breakdown(clean_text, single_window)
print("Read Complete")
print("Testing...")

#%%

for index in range(len(test_windows)):
    total_complexity = []
    start_clock = time.clock()
    list_breakdown(clean_text, test_windows[index])
    print("")
    print("\tWindow Value: %s" % (test_windows[index]))
    print("\tTime: %s Seconds" % (time.clock() - start_clock))

print("\nTesting Complete")