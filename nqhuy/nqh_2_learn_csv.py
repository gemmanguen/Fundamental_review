# -*- coding: utf-8 -*-
"""
@author: nqhuy
@date: 7/5/2022

A2  -Study the *csv file and its properties, and python library to read/write csv file. 
    -Make one csv file for example (monthly-car-sales.csv), print out its properties such as data shape, plot series.
"""
#--------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
#--------------------------------------------------
def save_csv(data):
    cars = pd.DataFrame(data, columns=['month', 'sales'])
    cars.to_csv('monthly-car-sales.csv', index=False)
    
def read(csv):
    return pd.read_csv(csv)

def display_csv():
    # data shape
    print('Shape of data:')
    print(read('monthly-car-sales.csv').shape)
    
    # plot series
    x = read('monthly-car-sales.csv')['month']
    y = read('monthly-car-sales.csv')['sales']
    plt.plot(x,y)
    plt.show()
    
#------------------------------------------------------
def testbench1():
    data=[['January','5'],
          ['February', '20'],
          ['august', '10']]
    save_csv(data)
    display_csv()
#----------------------------------------------------
if __name__=='__main__':
    testbench1()
    