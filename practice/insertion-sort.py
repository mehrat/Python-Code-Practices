#!/bin/python

def print_list(a):
    for i in a:
        print i,
    print

def insertionSort(ar):

    val = ar[len(ar)-1]
    ind = 0
    for i,j in enumerate(ar):
        if j > val:
            ind = i
            break;
    j = len(ar)-1
    while j > ind:
        ar[j]=ar[j-1]
        print_list(ar)
        j= j-1

    ar[ind]=val
    print_list(ar)
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
print insertionSort(ar)