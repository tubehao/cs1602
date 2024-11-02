# ilist = iter([-1,1,-2, 3, 4])
# print(next(ilist))
# print(next(ilist))
# print(next(ilist))
# print(next(ilist))

# m = [[1,2,3],[4,5,6],[7,8,9]]
# g = (sum(row) for row in m)
# print(next(g))
# print(next(g))
# print(next(g))

# class my:
#     def __init__(self, a = 0):
#         self.a = a
#     def __iter__(self):
#         self.a = 1
#         print('iter')
#         return self
#     def __next__(self):
#         if self.a <= 7:
#             print(('nex'))
#             x = self.a 
#             self.a += 1
#             return x
#         else:
#             raise StopAsyncIteration()
# myclas = my()
# for x in myclas:
#     print(x)

# def make(n):
#     def action(x):
#         return x**n
#     return action
# f1 = make(2)
# print(f1(2))

# lst1 = [1,2,3]
# lst2 = [2,3,4]
# lst1.extend(lst2)
# print(lst1.index(2))
# lst1.insert(2,4)
# lst1.remove(2)
# lis1.reverse()
# lst1.sort(reverse=1)
# print(lst1)

# st = ''
# seq = ('a', 'b', 'c')
# print(st.join(seq))

# str = "www.runoob.com"
# print(str.partition("."))

# str = "guanhao is liuhao's father father father father father"
# print(str.replace('father', 'grandpa', 3))
# print(str.find('a', 0, 6))
# print(str.index('a', 0, 6))
# print(str.split(' ', 6))

# import copy
# a = set('123')
# a.add(5)
# a.remove(2)
# a.update([10,12])
# b = copy.deepcopy(a)
# b.clear()
# print(chr(44))
# print(ord('a'))

# se = {1,2,4,6,5}
# print(sorted(se))

# lst1 = [1,2]
# lst2 = [3,4]
# print(list(zip(lst1,lst2)))

# s = 'spam'
# for (offset, item) in enumerate(s):
#     print(f'{item} in {offset}')

# exec('ax = 0')
# exec('print(ax)')

# lst1 = [1,2]
# del(lst1[0])
# print(lst1)

# lst1 = [1,2]
# reversed(lst1)
# print(list(reversed(lst1)))