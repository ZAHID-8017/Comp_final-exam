import numpy as np
import matplotlib.pyplot as plt
import time
n=10000

def f(R,m):
    i=0
    while(i<len(R)):
        if (R[i]==m):
            print(m, "is found in the array again at position at i=",i)
            break
        i+=1
    else:
        print(m,"is not found anywhere")
    return " "
a = 7
c = 7
m = 10
x0 = 7
x=7

rand_numbers = []
for i in range(n):
    x  = (a*x + c)%m
    rand_numbers.append(x)
#print(rand_numbers)
f(rand_numbers,x0)
#example for seed not appearing again   

a1=1664525
c1=1013904223
m1=4294967296
x1=1
x01=x1
rand_numbers1 = []
for i in range(n):
    x1  = (a1*x1 + c)%m1
    rand_numbers1.append(x1)
f(rand_numbers1,x01)





























    
