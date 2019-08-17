#!/usr/bin/python3

import random
import sys


def isSorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
        else:
            pass        
    return True

def StupidSort(arr): #Shuffles list until it's sorted
    while True:
        if isSorted(arr) == True:
            return arr
        else:
            random.shuffle(arr)

def genList(n):
    ls = []
    for i in range(n):
        ls.append(random.randint(0,100))
    return ls

if len(sys.argv) >= 1:
    n = int(sys.argv[1])
else:
    n = input("How long should the list be? ")

ls = genList(n)
print("===OLD LIST===\n",ls)
ls = StupidSort(ls)
print("\n=SORTED  LIST=\n",ls)
