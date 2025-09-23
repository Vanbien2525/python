import numpy as np
import matplotlib.pyplot as pl

a = np.array([1, 2, 3, 4, 5])
b = np.array([7, 8, 9, 10, 11])
for i in a:
    print(i)
    
print()
print(a[-1])
print(dot := a @ b)

pl.plot(a, b, 'go-')
pl.show()