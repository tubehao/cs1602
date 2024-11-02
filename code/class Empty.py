# # class Empty:
# #     pass
# # e = Empty()
# # print(e)
# # print(type(e))
# # print(id(e))

# # a = int()
# # print(a)

# # x=eval(input())
# # print(type(x),x)

# # class Empty:
# #     pass



# # def test_id(a, b,c):
# #     print("{}{}{}".format(id(a), id(b), id(c)))



# # e1 = Empty()

# # e1.a = [1]
# # e1.b = [1]
# # e1.c = [1]
# # e2 = Empty()
# # e2.a = [1]
# # e2.b = [1]
# # e2.c = [1]
# # a, b, c = 1,1,1
# # test_id(a, b,c)
# # test_id(e1.a,e1.b,e1.c)
# # test_id(e2.a,e2.b,e2.c)
# # print(type(e1),type(Empty))



# # class TestInit:
# #     def __init__(self):
# #         print("__init__is called automatically")
# #         print( "self id: {}".format(id(self)))
# #         print("__init__(exit)")



# # test1 = TestInit()
# # print(id(test1))

# # test2 = TestInit()
# # print(id(test2))

# # class Point:
# #     def __init__(self,x,y):
# #         self.x, self.y = x,y

# # def print_point_id(pt):
# #     print(id(pt), id(pt.x),id(pt.y))
# # def print_point(pt):
# #     print(pt.x, pt.y)
# # pt1 = Point(3,4)
# # pt2 = Point(3,4)
# # print_point(pt1)
# # print_point(pt2)
# # print_point_id(pt1)
# # print_point_id(pt2)
# # print(pt1.x*pt2.y - pt1.y*pt2.x, pt1.x + pt2.y)
# # pt1.x = -1
# # pt2.y ="Hello"
# # print_point(pt1)
# # print_point(pt2)


# class Triangle:
#     def __init__(self,a=0,b=0,c=0):
#         self.a, self.b, self.c = a, b, c
#     def is_valid(self):
#         return self.a>0
#     def set_edges(self,a,b,c):
#         self.a, self.b, self.c = a, b ,c
#     def area(self):
#         q = (self.a+self.b+self.c)/2
#         return (q*(q-self.a)*(q-self.b)*(q-self.c))**0.5
#     def print(self):
#         print("triangle: {}, {}, {}".format(self.a,self.b,self.c))
#     def print_area(self):
#         print(("Area: {:.3f}".format(self.area())))
# t1 = Triangle()
# t1.set_edges(3,4,5)

# if t1.is_valid():
#     t1.print()
#     t1.print_area()



# class vector:
#     def __init__(self):
#         self.L, self.a, self.ans, 
#     def leng(self):
#         while x<len(self):
#             L += self[x]**2
#         return L**0.5
#     def print_length(self):
#         print(self.leng())
#     def angle(self):
#         a = self
#         for x in a:
#             x = x/a.leng()
#         return a
#     def print_angle(self):
#         print(self.angle())
#     def dot(self,other):
#         ans=0
#         while x <= len(self):
#             ans += self[x]*other[x]
#         return ans
#     def scale(self,ratio):
#         for x in self:
#             x *= ratio
#         return self   
#     def is_orthogonal(self):
#         return self.dot() == 0
# x=eval(input())




class Person:
    def __init__(self,name, job=None, pay=0):
        print("Init: Person"+name)
        self.name = name
        self.job = job
        self.pay = pay
    def get_last_name(self):
        return self.name.split()[-1]
    
    def get_raise(self, percent):
        self.pay = int(self.pay * (1+percent))
    def __repr__(self):
        return '[person: {:s}, {:d}]'.format(self.name, self.pay)



class Manager(Person):
    def __init__(self, name, pay, id):
        print("Init:Manager"+name)
        Person.__init__(self, name, 'mgr', pay)
        self.id = id
    
    def give_raise(self, percent, bonus=0.1):
        Person.give_raise(self, percent+bonus)

    def __repr__():
        return "[Managere: {:s}{:d}]".format(self.name, self.pay)



roger = Manager("Roger Chen", "manager", 100000)
print((roger.name, roger.job, roger.pay))
print(roger.get_last_name())
roger.get_raise(percent=0.1)
print(roger)