#!/usr/bin/python

def f(n):
    return (n-1) * 0.8

def f6(n):
    for i in range(6):
        n = f(n)
    return n

def is_int(n):
    return abs(n-int(n)) < 0.0000001

n = 96
while(not is_int(f6(n))):
    n = n + 1

print n 


