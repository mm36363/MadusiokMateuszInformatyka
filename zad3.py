# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
suma = 0  
licznik = 0

for num in range(start, end + 1):
      
    if num % 2 != 0:
        print(num, end = " ")  
        suma = num + suma
        licznik = licznik + 1 
print(end = "\n") 
print("Srednia: ") 
print(suma/licznik , end = "\n") 

       