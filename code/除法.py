def div_list(x,y):
    if not com(x, y):
        return 
    else:
        x1 = copy.deepcopy(x)
        y1 = copy.deepcopy(y)
        s,m = 0,0
        # i=0
        while com(x1, mult(y1, 10)) and com(x1, mult(y1, 10))!=2:#除数补零
            y1.insert(0, 0)
        while com(x1, y1):#减到不能再减
            x1 = sub_list(x1, y1) 
            s += 1
        z[len(y1)-1] = s#结果的第i位
        # l_2=len(y)
        # for i in range(len(x)-1,len(x1),-1):

        # if len(x1)>=len(x):#把被除数剩下的一位加到下一位
        #     x1[len(x1)-2] += x1[len(x1)-1]*10
        #     del x1[len(x1)-1]
        # else:#如果就剩了就把
        #     z[1]=z[0]//10
        #     z[0]%=10
        
        div_list(x1, y)#对下一位进行除法
        
        while -1 in z:
            z.remove(-1)
        while z[len(z)-1] == 0:
            del z[len(z)-1]  
        return z
    return z
        # chang -= 1
        # z[s-1] = div_list(x1, y)
