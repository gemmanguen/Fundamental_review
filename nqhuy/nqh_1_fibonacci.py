# -*- coding: utf-8 -*-
"""
@author: nqhuy
@date: 7/5/2022

A1  -Write the Fib(n) function to return the n-th Fibonasi.
    -Using above Fib() to show n numbers of Fibonasi sequence.
"""
#------------------------------------------------------------
def nth_fibon(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return nth_fibon(n-1)+nth_fibon(n-2)
    
def display_fibo_seq(n):
    for i in range(1,n+1):
        print(nth_fibon(i), end=" ")
        
#----------------------------------------------------
def testbench1():
    n=20
    display_fibo_seq(n)
#----------------------------------------------------
if __name__=='__main__':
    testbench1()