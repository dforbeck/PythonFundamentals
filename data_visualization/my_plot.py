import matplotlib.pyplot as plt
import numpy as np

import csv
import pprint
from datetime import datetime


with open('data.csv', newline='') as data:
    data_reader = list(csv.reader(data))

    date = data_reader[0].index('DATE')
    hws = data_reader[0].index('HourlyWindSpeed')
    hdpt = data_reader[0].index('HourlyDewPointTemperature')


    # my_data = [] # where store the data of two columns
    my_x_values = []
    my_y_values = []
    my_other_y_values = []

    for i in data_reader[1:]: # from position 1 (vs. 0, skip headers) to end.
        # x = i[date] #  i has the list row, want the 1 column
        x = datetime.strptime(i[date],'%Y-%m-%dT%X')
        y = i[hws] #  i has the list row, want the 56 column
        
        try:
            y = int(i[hws])
            d= int(i[hdpt])
        except Exception:
            continue
        
        #my_data.append((x,y)) # appending tuple of x and y
        my_x_values.append(x)
        my_y_values.append(y)
        my_other_y_values.append(d)

    plt.subplot(2, 1, 1)  # if take this out it superimposes
    plt.plot(my_x_values, my_y_values, color='blue')
    plt.subplot(2, 1, 2) # if take this out it superimposes
    plt.plot(my_x_values, my_other_y_values, color='green')

    plt.show()

    # print(len(my_data))

    # print(type(data_reader[0].index('DATE'))) 
    # index above finds the index of that column, which is 1
    # pprint.pprint(data_reader[0].index('HourlyWindSpeed')) 
    # index above finds the index of that column, which is 56
    
    # print(datetime.strptime(data_reader[300][1],'%Y-%m-%dT%X'))
    
    # for row in data_reader:
    #     print(row)

# #x = np.linspace(0,2,100)

# plt.plot(x, x, label='linear')
# #plt.plot(x, x**2, label='quadratic')
# #plt.plot(x, x**3, label='cubic')

# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title('Simple plot')
# plt.legend()

# plt.show()