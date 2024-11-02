import copy
def strlist(x):
    lst = [0]*len(x)
    for i in range(len(x)):
        lst[i] = int(x[len(x)-1-i])
    return lst

def list_str(x):
    s = str(x)[::-1]
    y = s.replace('[', '')
    y = y.replace(']', '')
    y = y.replace(',', '')
    y = y.replace(' ', '')
    return y

def add_list(x,y):
    z = [0]*(max(len(x), len(y))+1)
    for i in range(len(z)):
        if i<len(x):
            z[i] += x[i]
        if i<len(y):
            z[i] += y[i]
    for i in range(len(z)-1):
        z[i+1] += z[i]//10
        z[i] %= 10
    if z[len(z)-1] == 0:
        del z[len(z)-1]
    return z

def sub_list(x, y):
    z = [0]*(max(len(x), len(y)))
    for i in range(len(z)):
        if i<len(x):
            z[i] += x[i]
        if i<len(y):
            z[i] -= y[i]
    for i in range(len(z)-1):
        if z[i] < 0:
            z[i] += 10
            z[i+1] -= 1
    while z[len(z)-1] == 0 and len(z)>1:
        del z[len(z)-1]  
    return z




def mult(x,y):
    z = [0]*(len(x)+1)
    i = 0
    while y:
        z = add_list(z, x)
        y -= 1
    if z[len(z)-1] == 0:
        del z[len(z)-1]  
    return z
def mul_list(x,y):
    z = [0]*(len(x)+1)
    i=0
    while i < len(y):
        z = add_list(z, mult(mult(x,y[i]), 10**i))
        i += 1
    while z[len(z)-1] == 0 and len(z)>1:
        del z[len(z)-1]  
    return z

def com(x,y):
    z = sub_list(x, y)
    b = 0
    for i in z:
        if i<0:
            return 0
    for i in z:
        if i != 0:
            b = 1
    if b == 0:
        return 2
    return 1

def div_list(x,y):
    if not com(x, y):
        return 
    else:
        x1 = copy.deepcopy(x)
        y1 = copy.deepcopy(y)
        s,m = 0,0
        while com(x1, mult(y1, 10)) and com(x1, mult(y1, 10))!=2:#除数补零
            y1.insert(0, 0)
            m += 1
        while com(x1, y1):#减到不能再减
            x1 = sub_list(x1, y1) 
            s += 1
        z[m] = s#结果的第i位
        div_list(x1, y)#对下一位进行除法
        i = len(z)-1
        while i:
            if z[i] == -1:
                del z[i]
            elif z[i] != -1:
                break
            i -= 1
        for j in range(len(z)):
            if z[j] == -1:
                z[j] = 0
        while z[len(z)-1] == 0 and len(z)>1:
            del z[len(z)-1]  
        return z

def add(str1,str2):
    lst1 = strlist(str1)
    lst2 = strlist(str2)
    sum = add_list(lst1,lst2)
    list_str(sum)
    return list_str(sum)

def sub(str1,str2):
    lst1 = strlist(str1)
    lst2 = strlist(str2)
    if int(str1) > int(str2):
        sum = sub_list(lst1,lst2)
        return list_str(sum)
    if int(str1) == int(str(2)):
        return str(0)
    if int(str1) < int(str2):
        sum = sub_list(lst2,lst1)
        return '-'+list_str(sum)

def mul(str1,str2):
    lst1 = strlist(str1)
    lst2 = strlist(str2)
    sum = mul_list(lst1,lst2)
    list_str(sum)
    return list_str(sum)

def div(str1,str2):
    lst1 = strlist(str1)
    lst2 = strlist(str2)
    global z  
    z = [0]*(len(str1)+1)
      
    div_list(lst1,lst2)
    sum = z
    s = list_str(sum)
    mod = 0
    mod = sub(str1, mul(s, str2))
    return s, mod
    

def pow(x,y):
    s = y
    sum = '1'
    while s > 0:
        sum = mul(sum, x)
        s -= 1
    return sum
# x = input()
# y = input()
print(add('22222222222222', '8773849905050505'))
print(sub('11111111', '9877344555'))
print(sub('345676778778', '222222'))
print(mul('123456', '789'))
print(div('8773849905050505', '123')[0],div('8773849905050505', '123')[1])
print(pow('2', 66))
print(add(pow('2', 100), pow('3', 50)))
print(sub(add(pow('2', 100), mul('123456', '789')), div('8773849905050505', '123')[0]))
# print(div(x, y))

def myfunc1():
    x="John"
    def myfunc2():
        nonlocal x
        x="hello"
    myfunc2()
    return x
print(myfunc1())


