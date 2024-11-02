# def test(x, lst = None):
#     if not lst:
#         lst = []
#     lst.append(x)
#     return lst
# print(test(1))
# print(test(2))
# print(test(3))

# x = lambda a : a + 10
# print(x(5))

# f = lambda lst,x: lst.append(x) or lst
# lst = list(range(11))
# print(f(lst, -12))

# print(sorted([1,2,3,-1,20,-5], key = lambda x: x**2))

# import random
# lst = list(range(7))
# random.shuffle(lst)
# print(lst)

# lst = list(range(2020))
# print(random.choice(lst))

# spl = random.sample(lst, k = 4)
# print(spl)

# f = open("file.txt", 'wb')
# print(f.name)
# print(f.closed)
# print(f.mode)
# f.close()

# f = filter(bool, ['9',''])

# print(list(f))

# import functools
# print('the sum of the list elements is', end = ' ')
# print(functools.reduce(lambda x,y: x if x>y else y, [1,3,5,6,2]))

# def f():
#     s = 100
#     s += 200
#     print(s)
#     del s 
#     print(s)

# s = 100
# f()

a = (1,2,3)
print(a[2:1:-1])