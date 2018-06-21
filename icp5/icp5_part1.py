# importing numpy library
import numpy as np

# importing mat plot library for displaying the plot with X against Y
import matplotlib.pyplot as plt

x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([1,3,2,5,7,8,8,9,10,12])
x_mean=np.mean(x)
y_mean=np.mean(y)

B1= np.sum((x-x_mean)*(y-y_mean))/np.sum(np.power(x-x_mean,2))
B0= y_mean-(B1*x_mean)

print("B0=", B0)
print("B1 =",B1)

# linear regression : y=mx+c slope and a constant
formula=(B1*x)+B0

print(formula)
plt.plot(x,y,formula)
plt.show()