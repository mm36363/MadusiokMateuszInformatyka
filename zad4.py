# -*- coding: utf-8 -*-
"""
Created on Sat May 15 09:10:32 2021

@author: mateu
"""

def bubbleSort(arr):
    n = len(arr)  
    for i in range(n-1):
           for j in range(0, n-i-1):
  
              if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
  
arr = [9,4,7,3,1]
  
bubbleSort(arr)
  
print ("Posortowana tablica:")
for i in range(len(arr)):
    print ("%d" %arr[i]), 