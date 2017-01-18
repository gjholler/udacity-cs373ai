#!/usr/bin/python

def f(n):
    return (n-1) * 0.8

def f6(n):
    for i in range(6):
        n = f(n)
    return n

print f6(96.)


