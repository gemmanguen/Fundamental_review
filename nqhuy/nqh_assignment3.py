"""
@author: nqhuy
@date  : 

A3  -Study about Sine wave and its properties (Frequency, time, phase).
    -Plot a sine wave by python with: (Sampling frequency = 40000Hz; Frequency = 1000Hz; phase = 0; Numbers of samples = 80)	

"""
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
#------------------------------------------------------------------------------       
def plot_sine(x,y):
    plt.plot(x,y)
    plt.show()   
#------------------------------------------------------------------------------
def testbench1():
    f   = 1000               #frequency
    x   = np.arange(80)     #samples
    fs  = 40000            #Sampling frequency
    y   = np.sin(2*np.pi*f*x/fs)
    plot_sine(x,y)
#------------------------------------------------------------------------------   
if __name__ == "__main__":
    testbench1()
#------------------------------------------------------------------------------   