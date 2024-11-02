import time
def pm1():
    time_start=time.time()
    number_pn = 0
    lst=[1]*1000001
    for x in range(1,1000001):
        for i in range(2,x):
            if x%i == 0:
                lst[x] = -1
    for x in range(1,1000001):
        if lst[x] != -1:
            number_pn += 1

    time_end = time.time()
    return time_end-time_start,number_pn-1


def pm2():
    time_start = time.time()
    number_pn = 0
    lst=[1]*1000001
    for x in range(1,1000001):
        for i in range(2,int(x**0.5)+1):
            if x%i == 0:
                lst[x] = -1
    for x in range(1,1000001):
        if lst[x] != -1:
            number_pn += 1
    time_end = time.time()
    return time_end-time_start,number_pn-1


def pm3():
    time_start = time.time()
    number_pn = 0
    lst=list(range(0,1000001))
    for x in range(6,1000001):
        if x%6 == 2 or x%6 == 0 or x%6 == 3 or x%6 == 4:
            lst[x] = -1

    for x in range(1,1000001):
        if lst[x] != -1:
            for i in range(2,int(x**0.5)+1):
                if x%i == 0:
                    lst[x] = -1
                    break
    for x in range(2,1000001):
        if lst[x] != -1:
            number_pn += 1
    time_end = time.time()
    return time_end-time_start,number_pn


def pm4():
    time_start = time.time()
    primes=[1]*1000000
    primes[0]=primes[1]=0
    for i in range(2,int(1000000**0.5)+1): 
        if primes[i]:
            primes[i*i:1000000:i]=[0]*((1000000-1)//i-i+1) 
    time_end=time.time()
    return time_end-time_start, sum(primes)




def mi(d,a,p):
    b=[]
    while a>0:
        if a%2==1:
            b.append(d)
            a-=1
        else:
            d=d*d%p
            a=a/2
    d=1
    for i in b:
        d=d*i%p
    return d

def pr(i,n):
    u=n-1
    t=0
    while u%2 != 1 and u != 0:
        u //= 2
        t+=1
    p=mi(i,u,n)
    q=(p**2)%n
    i=1
    while i<=t:
        if q%n == 1:
            if p%n != 1 and p%n != n-1:
                return 0
            return 1
        p=q
        q=(p**2)%n
        i+=1
    return 0

def pm5():
    lst=[0]*(z+1)
    time_start = time.time()
    for i in range(2,z+1):
        lst[i] = pr(2,i) and pr(3,i) and pr(5,i)
    time_end=time.time()
    return time_end-time_start, sum(lst)+3
z=1000000
print(pm5())