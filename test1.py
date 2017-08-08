import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
y = np.matrix([[242,4,3],[321,323,434],[231,234,453]])
x = pd.DataFrame(data=np.array(np.mat('2 1 3 ;2 3 4;4 2 4')))
print(y)
print(x)
plt.plot(x,y)
plt.show()
f = x.dtypes
for i in f:
    print(i)
print(x.describe())
