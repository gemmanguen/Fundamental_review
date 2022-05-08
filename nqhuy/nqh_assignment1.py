# -*- coding: utf-8 -*-
"""
@author: HaiDuc

Problem:A1  
    -Write the Fib(n) function to return the n-th Fibonasi.
    -Using above Fib() to show n numbers of Fibonasi sequence.
"""
#------------------------------------------------------------------------------
def printFibSequence(n):
    if(n<=0):
        return
    if(n==1):
        print(1)
    elif(n==2):
        print("1 1")
    else:
        preNumber1=1
        preNumber2=1
        print("1 1", end=" ")
        for i in range(3,n+1):
            fibon=preNumber1+preNumber2
            print(fibon, end=" ")
            preNumber2=preNumber1
            preNumber1=fibon
#------------------------------------------------------------------------------        
def testbench1():
   printFibSequence(6)
#------------------------------------------------------------------------------   
if __name__ == "__main__":
    testbench1()
#------------------------------------------------------------------------------   