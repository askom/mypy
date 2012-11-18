# module smooth.py
from numpy import *

def med3(x):
        y = vstack((x[:-2],x[1:-1],x[2:]))
        y = y.sum(axis=0)-(y.min(axis=0)+y.max(axis=0))
        return hstack((x[0],y,x[-1]))

def med3n(x,n=1):
     while n>0:
        y = vstack((x[:-2],x[1:-1],x[2:]))
        y = y.sum(axis=0)-(y.min(axis=0)+y.max(axis=0))
    n-=1
        y=hstack((x[0],y,x[-1]))
    x=y
     return y

def hann(x):
    y=vstack((x,roll(x,-1),roll(x,-2)))
    y=dot([0.25,0.5,0.25],y)
    return hstack((x[0],y[:-2],x[-1]))

