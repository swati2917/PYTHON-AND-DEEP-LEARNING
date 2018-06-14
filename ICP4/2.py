import numpy as n

#Creating  a 10x10 array with random value


r= n.random.rand (10, 10)
min,max=r.min(), r.max()
print (r)


# finding the minimum and maximum values in each row
print ("min:", min ,"max:", max)