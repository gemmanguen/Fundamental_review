"""
A2  -Study the *csv file and its properties, and python library to read/write csv file. 
    -Make one csv file for example (monthly-car-sales.csv), print out its properties such as data shape, plot series.
"""

import pandas as pd
import matplotlib.pyplot as plt

data=[['January','5'],
      ['February', '20'],
      ['august', '10']]
cars = pd.DataFrame(data, columns=['month', 'sales'])
cars.to_csv('monthly-car-sales.csv', index=False)

cars_data = pd.read_csv('monthly-car-sales.csv')
# data shape
print('Shape of data:')
print(cars_data.shape)

# plot series
x=cars_data['month']
y=cars_data['sales']
plt.plot(x,y)

plt.show()
