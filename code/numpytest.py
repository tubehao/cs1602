import numpy as np
# a = np.empty([3,3], dtype = int)
# print(a)

# x = np.zeros(5)
# print(x)

# y = np.zeros((2,2), dtype = [('x', 'i4'), ('y' ,'i4')])
# print(y)

# x = np.ones([2,2], dtype = int)
# print(x)

# x = np.ones(5)
# print(x)

# s = b'Hllo World'
# a = np.frombuffer(s,dtype = 'S1')
# print(a)

# list = range(5)
# it = iter(list)
# x = np.fromiter(it, dtype=float)
# print(x)

# x = np.arange(10,20,2)
# x = np.linspace(1, 10, 10).reshape([10,1])
# x = np.logspace(0,9,10,base=2)
a = np.arange(10)
s = slice(2,7,2)

print(a[s])