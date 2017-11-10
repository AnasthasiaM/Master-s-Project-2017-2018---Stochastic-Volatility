# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 21:58:04 2017

@author: Ana
"""

"""
relative error in monte carlo remains approx the same 
as you increase number of dimensions
similar to rectangular formation of integral but
integral use rectangles that are randomly positioned
Area of one rectangle:

A = f(x)*((b-a)/N)
A = area of one rectangle
b = upper limit
a = lower limit
N = number of rectangles

Then sum(A) in order to give integral usually
"""
#from numpy import *

#N = 100
#a = -5000
#b = 5000
##
#def f(x,a,b,):
#"""
#simple quadrature using rectangles 
#    q = x**2
#    return q
#    
##x = (a - b)*random.random(N)
##In order to get monte carlo from normal rectangular summation
##just multiple by random number to get midpoint of x
##x = linspace(a, b, N) 
#
#y = f(x)
#A = y*((b-a)/N)
#
#integral = sum(A)
#
#print(integral)

#
#    
#def monte_carlo(a,b,N):
#    def f(x):
#        f = exp(-(x**2))
#        return f
#    
#    Atotal = 0
#    for i in range(1,N):
#        x = a + (b-a)*random.random()
#        y = f(x)
#        A = y*(b-a)/N
#        Atotal = Atotal+ A
#    
#    return Atotal
#    
#def try_work(a,b,N):
#    """
#    This code allows us to create a cut off point where we can estimate the 
#    integral with enough accuracy
#    this workd on the premise that
#    i(x)-i(2*x)<delta*i(2*x)
#    """
#    delta = 1e-5
#    new=monte_carlo(a,b,N)
#    old=-new
#    while(fabs(new-old)>delta*fabs(new)):
#        old=new
#        N=2*N
#        new=monte_carlo(a,b,N)
#    return new
# 
#print(try_work(a,b,8))    
#
#
#x = random.normal(0,1,50)
#mean_x = sum(x)
#var_x = var(x)

import numpy as np
import matplotlib.pyplot as plt

N=100000
sigma=1.5
mu=2

xx = np.random.normal(mu,sigma,N)
#xx = (np.arange(0,N,1))**2

plt.hist(xx,normed=True)
x=np.arange(-4,4,.01)
plt.plot(x,np.exp(-(mu-x)**2/2./sigma**2)/np.sqrt(2*np.pi*sigma**2),'g-')
plt.show()


print ("<x>")
print (np.mean(xx),np.var(xx))
print ("compared to input mu=",mu," and sigma^2=",sigma**2)
print ("<x^2>")
print (np.mean(xx**2),np.var(xx**2))
print ("expectation",mu**2+sigma**2)
print ("<x^3>")
print (np.mean(xx**3),np.var(xx**2))
print ("expectation",mu*((mu**2)+(3*sigma**2)))
#print (np.mean(xx**2+xx),np.var(xx**2+xx))



   