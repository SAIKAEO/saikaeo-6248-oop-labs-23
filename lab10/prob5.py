import numpy as np
number = 10 + 2*np.arange(20).reshape((4, 5))

print(number)
print(number[:, 2])
number[3, :] = np.arange(1, 6)
print(number)
