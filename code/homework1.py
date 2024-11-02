# def ham(n, x, y, z):
#     if n==1:
#         print(f'{x}->{z}')
#         return
#     ham(n-1, x, z, y)
#     print(f'{x}->{z}')
#     ham(n-1, y, x, z)
#     return

# n=int(input())
# x, y, z = 'A', 'B', 'C'
# ham(n, x, y, z)



# def ham(n, x, y, z):
#     # x,z不相邻
#     if n==1:
#         print(f'{x}->{y}')
#         print(f'{y}->{z}')
#         return
#     ham(n-1, x, y, z)
#     print(f'{x}->{y}')
#     ham(n-1, z, y, x)
#     print(f'{y}->{z}')
#     ham(n-1, x, y, z)
#     return

# n=int(input())
# x, y, z = 'A', 'B', 'C'
# ham(n, x, y, z)


# x=list(range(1,int(input())+1))
# i=0
# while len(x) > 1:
#     i += 1
#     if i >= len(x):
#         i = 0
#     x.pop(i)
#     if i >= len(x):
#         i = 0
# print(i+1)


# def cir(n):
#     if n == 1:
#         return 1
#     elif n%2==0:
#         return 2*cir(n//2)-1
#     else:
#         return 2*cir(n//2)+1
#     return ans
# ans=0
# x=int(input())
# print(cir(x))

n=int(input())
m=0
while m >= 0:
    if 2**m <= n < 2**(m+1):
        n -= 2**m
        break
    m+=1
print(2*n+1)