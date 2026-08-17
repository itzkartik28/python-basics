import numpy as np

a=np.array([10,20,30])

#aliasing
b=a
b[0]=100

print("after aliasing")
print("array a:",a)
print("array b:",b)

#copying
c=a.copy()
c[1]=200

print("after copying")
print("array a:",a)
print("array b:",c)