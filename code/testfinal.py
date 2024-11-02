# a = set('\this problem is very easy\\\n')
# print(len(a))

# print("123123123".count("123123"))

# print()
# ["abc"] == list('abc') 			
# # {"abcd"} == dict('abcd')
# ("a") == set('a')
# "ab" != str('ab')

# a, b = [1] * 3, [[1]] * 3
# a[0], b[0], b[1][0] = 5, 5, 5
# print(a, b)

# print(2 < 5 > 0)

# def Fibonacci(n):
# 	if n <= 1:
# 	    return 1
# 	return Fibonacci(n-1) + Fibonacci(n-2)

# modes = ['w', 'w+', 'a', 'r']
# for i in range(20):
#     mode = modes[i % 4]
#     with open('output.tx', mode) as f:
#         if f.writable():
#             for j in range(i):
#                 f.write(str(j) + '\n')


# print(list(range(0)))

# a=[i % 3 for i in range(0,5)]
# print(a)

# alist = [1,2,3,1,2]
# print({each for i, each in enumerate(sorted(alist)) if each == sorted(alist)[i+1]})

# print('{1} == {0}'.format(3, 5))


# a = open('123.txt', 'w')
# a.write('123')
# a.close()
# a = open('123.txt', 'w')
# a.write('456')
# a.close()

# print(max([ "PYTHON", "JAVASCRIPT", "PHP", "JAVA"]))

# a = [1,2,3,4,5]; a[0:3] = 3

# str = "\b".join(["S","J","T","U"])
# print(str)

# a = [1,2,3,4,5,6,7,8]
# x = len(a)
# r = 0
# for i in range(x):
#     print(a[i], end=",")
#     r += a[i]
#     del(a[0])
# print(r)

# for x in range(8):
#     if x == 6:
#         print(x, ': for x inside loop')
# print(x, ': x in global')

# myset = {'Github', 'StackOverflow', 'LeetCode'}
# print(myset.pop() in myset)

# class A:
#     def __init__(self, x, y):
#     	self.x, self.y = x, y 
# c = set()
# a = A(c, 3)
# b = a
# c.add(1)
# a.y, c = 2, set([2])
# print(a.x, a.y, b.x, b.y)


# with open('test.txt','r') as Fin:
#     next(Fin)
#     result = []
#     for line in Fin:
#         result.append(line.strip())
# print(result)

# X = set((1,))
# C = {(x, 1): [x] for x in range(5)}
# print('aaa'-'a')
# print((1, 3) + (2, 4))
# print(set([[1,2],[3,4]]))

# def distance(a, b):
#     return abs(a - b)

# def fold(seq, func):
#     if len(seq) == 1:
#         return seq[0]
#     else:
#         return func(seq[0], fold(seq[1:], func))

# print(fold([2, 1, 4, 3], distance))

# a = [[]] * 2
# b = [[] for i in range(2)]
# print(a[0] is a[1])
# print(b[0] is b[1])

# def f(seq):
#     for i, j in seq:
#         pass
# f([])   
# f([1, 2]) 
# f([[1, 2], [3, 4]])  
# print(True is False == False)

# string = 'HELLO WORLD'
# string_list = list(string)
# for i in range(len(string_list)-1, -1, -2):
#     string_list[i] = '*'
# new_string = ''.join(string_list)
# new_string.lower()
# print(new_string)

# print("SJTU" + "_nohtyP"[:0:-1] * 2)
# A = [[]]*3
# A[0].append(0)
# A[1] += [0]
# A[2] = A[2] + [0]
# print(A)

# def f(a):
#     return lambda x : x + a
# a = 1
# g = f(a)
# h = lambda x : x + a 
# a = 2
# print(g(0), h(0))

# print(type((1,)))

# a, b = 5, 1
# b, a = a+1, b-a+1
# a = b = a+1
# print(a, b)

# print(1+4*3/2**4 )

# L = ["SJTU", "Avracadavra", "ADU"]
# print((L[::5]))

# dt = {'1': (lambda x,y: x + y),
# 		'2': (lambda x,y: x - y),
# 		'3': (lambda x,y: x * y),
# 		'4': (lambda x,y: x ** y)
# 		}
# keylist= ['1', '3', '2', '4', '1', '2']
# x = keylist[-1]
# print(x, dt[x](10, 3))

# print(0 or '')

# a = [1,3,5,4,-6]
# a[2:4] = [3]
# print(a)

# st = '1m'
# print(st.isdigit())

# s = set((1,2,3))
# print(type(i) for i in s)

# exec('print("2")')

# print(range(2))

# lst = [1,1,2,1,3,1,4,1]
# for x in lst:
#     print(x)
#     x = -1
# print(lst)

# print(list(set(lst)))

# try:
#     raise NameError('hi')
# except NameError():
#     print("exeception")
#     raise

# x = 10
# def powx(a,x = x):
#     return a**x
# print(powx(2))
# x = 9
# print(powx(2))

# lst = [2,3,4,5,6]
# a = lst[0:1]
# b = lst[0:2]
# print(id(a),id(b))

def f():
    s = 100
    s+=200
    print(s)
    del s
    print(s)
s = 100
f()

# def g():
#     # global s
#     # print(s)
#     s = '111'
#     print(s)

# # s = 'jsfdjsj'
# g()
# print(s)

# def foo(x,y):
#     global a
#     a = 42
#     x,y = y,x
#     b = 33
#     b = 17
#     c = 100
#     print(a,b,c,x,y)

# a,b,x,y = 1,15,3,4
# foo(17, 4)
# print(a,b,x,y)

# def f():
#     city ="Hamburg"
#     def g():
#         global city
#         # city = "Geneva"
#     print("Before calling g: " + city)
#     print("calling g now: ")
#     g()
#     print("After calling g: " + city)
# f()
# print( "Value of city in main: " + city)

# def myfunc1():
#     x="John"
#     def myfunc2():
#         nonlocal x
#         x="hello"
#     myfunc2()
#     return x
# print(myfunc1())

# x = "g1"
# def g1():
#     def g2():
#         # nonlocal x
#         # global x
#         print("g2.{}".format(x))
#         x = "g2"
#         print("g2.{}".format(x))
#     global x
#     print(x)   
#     g2()
#     print(x)
#     x = "gg"
#     print(x)
# g1()

# from math import tan
# print(math.tan(2))

# def f(s):
#     if s == []:
#         return [[]]
#     return f(s[1:]) + [x + [s[0]] for x in f(s[1:])]
# print(f([1,2,3]))

# add = lambda x, y: x + y
# minus = lambda x, y: x - y
# multi = lambda x, y: x * y
# power = lambda x, y: x ** y

# def calc(operands, *operations):
#     for op in operations:
#         operands.append(op(operands.pop(), operands.pop()))
#     return operands[-1]
# print(calc([1,2,3,4,5],add,power,minus,multi))

# def f():
# 	s = 100
# 	s += 200
# 	print(s)
# 	del s
# 	print(s)

# s = 0
# f()
# class T:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

# a = T(1, 1)
# b = a
# b.a, a.b = 2, 3
# print(a.a, b.b)

# alist = [1, 2, "def" , 3, "abc"]
# b = (x for x in alist)
# next(b)
# aset, atuple = set(b), tuple(b)
# print(aset, atuple)

# print( 24 / 2 ** 4)

# s = 'the sky is blue'
# print(s[-4:], s[:-4])

# sentence = "hello 54749110 this is john"
# counter1, counter2, counter3 = 0, 0, 0
# for character in sentence:
# 	if character.isdigit():
# 		counter1 += 1
# 	if character.isalpha():
# 		counter2 += 1
# 	else:
# 		counter3 += 1
# print(counter1, counter2, counter3)

# def mypow():
# 	plist = []

# 	for i in range(3):
# 		plist.append(lambda x: x**i)	

# 	return plist

# for i in range(3):
# 	print(mypow()[i](2), end=" ")

# from functools import reduce
# alist = (4, 3, 7, -1) 
# print(reduce(lambda a, b: (a,b)[a<=b], alist))

# s = '1,2,3,4,5'
# print( [s.join('')])

# try:
#     # 1/0
#     int('s')
# # except ValueError():
#     # print(ValueErro)
# except TypeError():
#     print(typen)

# def foo(x: int):
#     if x <= 1: 
#         return x
#     left = 0
#     right = x
#     while left <= right:
#         mid = (left + right) // 2
#         if mid**2 < x and (mid + 1)**2 >= x:
#             return mid
#         elif mid**2 < x: 
#             left = mid + 1
#         elif mid**2 > x: 
#             right = mid - 1
# print(foo(36))

# a = set(1, 2, 3)
# a = set([1, 2, 3])
# a = {1, [2], 3}
# a = {1, ([2],), 3}

# L = ["SJTU", "Avracadavra", "ADU"]
# print(''.join(L[::9]))

# dt = {'1': (lambda x,y: x + y),
# 		'2': (lambda x,y: x - y),
# 		'3': (lambda x,y: x * y),
# 		'4': (lambda x,y: x ** y)
# 		}
# keylist= ['1', '3', '2', '4', '1', '2']
# x = keylist[-1]
# print(x, dt[x](10, 3))

# a = [1, 5, 4, 6, 8, 5, 3, 1, 3, 5, 7]
# # print(a[5:-2:1])
# print(a.sort())
# print(sorted(a))

# def Fibonacci(n):
#     if n <=1:
#         return 1
#     return Fibonacci(n-1)+ Fibonacci(n-2)
# print(Fibonacci(3))

# def f():
#     print(s)
#     s ="I love London!"
#     print(s)
# s = "I love Paris!"
# f()

# a = (2,)