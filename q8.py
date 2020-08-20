import math
import numpy as np

p=1

def f1(h):
    return (f(p) - f(p-h))/h

def f2(h):
    return (f(p+h) - f(p-h))/2*h

def f3(h):
    return (f(p-2*h) - 8*f(p-h) + 8*f(p+h) - f(p+2*h))/12*h

def f(x):
    return math.e**(-x**2)

h1=0.1
h2=0.05
h3=0.025
h4=0.0125

print("F1")
print("h=",h1,"// f(x)=",f1(h1))
print("h=",h2,"// f(x)=",f1(h2))
print("h=",h3,"// f(x)=",f1(h3))
print("h=",h4,"// f(x)=",f1(h4))

print("\nF2")
print("h=",h1,"// f(x)=",f2(h1))
print("h=",h2,"// f(x)=",f2(h2))
print("h=",h3,"// f(x)=",f2(h3))
print("h=",h4,"// f(x)=",f2(h4))

print("\nF3")
print("h=",h1,"// f(x)=",f3(h1))
print("h=",h2,"// f(x)=",f3(h2))
print("h=",h3,"// f(x)=",f3(h3))
print("h=",h4,"// f(x)=",f3(h4))