import matplotlib.pyplot as plt
import numpy as np

import csv
import pprint


with open('data.csv', newline='') as data:
    data_reader = list(csv.reader(data))
    pprint.pprint(data_reader[0])
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