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

# 6.1 involved problems
# print(bin(4))#二进制
# lst1 = [1,2,3,4]
# lst2 = [5,6,7,8]
# print(list(zip(lst1,lst2)))

# keys = [ 'spam', 'eggs ' , 'toast ' ]
# vals = [1,3,5]
# D3 = dict(zip(keys, vals))
# print(D3)

s = 'spam'
for ( offset, item) in enumerate(s):
    print(item,'appears at offset ' , offset)




# 7problems
# def perm(n):
#     if n == 1:
#         return [(1,)]
#     lst = perm(n-1)
#     ans = []
#     for x in lst:
#         for i in range(n):
#             newx = x[:i]+(n,)+x[i:]
#             ans.append(nx)
#     return ans

# def perm(n):
#     if n == 1:
#         return [(1,)]
#     lst = perm(n-1)
#     ans = []
#     for i in range(1,n+1):
#         for x in lst:
#             lt = list(x)
#             for j in range(n-1):
#                 if lt[j]>=i:
#                     lx[j] += 1
#             nx = (i,)+tuple(lx)
#             ans.append(nx)
#     return ans

# print(pow(2, 1234567))