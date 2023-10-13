'''1)a=int(input())
for i in range(a):
    for j in range(i+1):
        print("*",end='')
    print()
    
i/p: 4
o/p: 
*
* *
* * *
* * * *

2)a=int(input())
for i in range(a):
    print("* "* (i+1))
 
i/p: 4   
o/p:
*
* *
* * *
* * * *


3)a=int(input())
for i in range(a):
    for j in range(a-i):
        print(" ",end='')
    for k in range(i+1):
        print("* ",end='')
    print()

    
4)a=int(input())
for i in range(a):
   print(" "*(a-i)+"* "*(i+1))

for i in range(a):
   print(" "*(i+1)+"* "*(a-i))

i/p:4
o/p:

5)a=int(input())
for i in range(a):
    print(str(i+1)*(i+1))
    
    
6)a=int(input())
b=1
for i in range(1,a+1):
    print(b*i)
    b=(b*10)+1


7)a=int(input())
for i in range(1,a+1):
    print(((10**i)//9)*i)

i/p: 4
o/p:
1
22
333
4444

8)def cse():
    print("Hi")
def ece(x=10,y=20):
    print("Hello",x,y)
ece(5)
cse()


9)def cse(x):
    print("Hi")
    print(x)
def ece(x):
    print("Hello")
    cse(x+3)
    print(x)
ece(5)
cse(4)
print(2)

o/p:
Hello
Hi
8
5
Hi
8
4
2
 

10)def cse(x):
    if(x==0):
        return 0
    print(x)
    cse(x-1)
    print(x)
cse(4)

o/p:
    4
    3
    2
    1
    1
    2
    3
    4

11)def cse(x):
    if(x==0):
        return 0
    print(x)
    print(cse(x-1))
    print(x)
cse(4)

o/p:
4
3
2
1
0
1
None
2
None
3
None
4


12)def cse(x):
    if(x==0):
        return 0
    print(x)
    print(cse(x-1))
    print(x)
    return 18
cse(4)

o/p:
4
3
2
1
0
1
18
2
18
3
18
4


13)def cse(x):
    if(x==0):
        return 0
    return x+cse(x-1)
print(cse(4))

o/p:10


14)def cse(x):       ..........>Factorial
    if(x==0):
        return 1
    return x*cse(x-1)
print(cse(5))

o/p:120


15)def cse(x):
    if(x==1):
        return 1
    if(x==2):
        return 1
    return cse(x-1)+cse(x-2)
print(cse(4))

o/p:3


16)def cse(x):
    if(x==1):
        return 1                   ...........>Fibonacci
    if(x==2):
        return 1
    return cse(x-1)+cse(x-2)
for i in range(1,11):
    print(cse(i),end=" ")
    
o/p:1 1 2 3 5 8 13 21 34 55



.............................................................................................................




17)class cse:
    def qwer(self):
        print("Hi")         ...> If it contains self then it is a static method
a=cse()
a.qwer()                         If the variable is not linked to the object then it is static variable
cse.qwer(20)

o/p:
Hi
Hi


18)class cse:
    x=10
    def __init__(self):
        self.y=30
    def qwer(self):             Here x is a static variable and y is a non-static variable
        print("Hi")                   so we need to call y as a.y with object 
a=cse()                                    but we can call x as a.x or cse.x
a.qwer() 
print(cse.x,a.y)

o/p:
Hi
10 30


19)class cse:
    x=10
    def __init__(self):
        self.y=30
    def qwer(self):             
        print("Hi",self.y)                   
a=cse()                                  here  we can call y as a.y or self.y
a.qwer() 

o/p:
Hi 30


20)class cse:
    def __init__(self,k):
        self.y=k
    def qwer(self):             
        print("Hi",self.y)                   
a=cse(80)                                         
b=cse(12)
b.qwer() 
a.qwer()

o/p:
Hi 12
Hi 80


21)class node:
    def __init__(self,z):
        self.data=z
        self.next=None
class cse:
    def __init__(self,k):
        self.head=None
    def qwer(self,x):             
        self.head=node(x)                   
a=cse(80)                                         
b=cse(12)
b.qwer(20)
print(b.head.data)
print(b.head.next)

o/p:
20
None


22)class node:
    def __init__(self,z):
        self.data=z
        self.next=None
class cse:
    def __init__(self,k):
        self.head=None
    def qwer(self,x):                              ....>Single Linked list with 2 nodes
        if(self.head==None):
            self.head=node(x) 
        else:
            self.head.next=node(x)
a=cse(80)                                         
b=cse(12)
b.qwer(20)
b.qwer(30)
print(b.head.data)
print(b.head.next)
print(b.head.next.data)
print(b.head.next.next)

o/p:
20
<__main__.node object at ....
30
None


23)class node:
    def __init__(self,z):
        self.data=z
        self.next=None
class cse:
    def __init__(self):
        self.head=None
    def create(self,x):                                 To add nodes at the last
        if(self.head==None):
            self.head=node(x) 
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(x)
b=cse()
b.create(10)
b.create(20)
b.create(30)
b.create(40)
print(b.head.data)
print(b.head.next)
print(b.head.next.data)
print(b.head.next.next)
print(b.head.next.next.data)
print(b.head.next.next.next)
print(b.head.next.next.next.data)
print(b.head.next.next.next.next)

o/p:
10
<__main__>....
20
<__main__>....
30
<__main__>....
40
None



24)class node:
    def __init__(self,z):
        self.data=z
        self.next=None
class cse:
    def __init__(self):
        self.head=None
    def create(self,x):                                 
        if(self.head==None):
            self.head=node(x) 
        else:
            temp=self.head
            while(temp.next!=None):                    To add node at the front
                temp=temp.next
            temp.next=node(x)
    def add_front(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=node(x)
            temp.next=self.head
            self.head=temp
b=cse()
b.create(20)
b.create(30)
b.create(40)
b.add_front(10)
print(b.head.data)
print(b.head.next)
print(b.head.next.data)
print(b.head.next.next)
print(b.head.next.next.data)
print(b.head.next.next.next)
print(b.head.next.next.next.data)
print(b.head.next.next.next.next)


o/p:
10
<__main__>....
20
<__main__>....
30
<__main__>....
40
None



25)class node:
    def __init__(self,z):
        self.data=z
        self.next=None
class cse:
    def __init__(self):
        self.head=None
    def create(self,x):                                 
        if(self.head==None):
            self.head=node(x)                           To display the linked list
        else:
            temp=self.head
            while(temp.next!=None):                 
                temp=temp.next
            temp.next=node(x)
    def add_front(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=node(x)
            temp.next=self.head
            self.head=temp
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end="->")
            temp=temp.next
b=cse()
b.create(20)
b.create(30)
b.add_front(50)
b.create(40)
b.add_front(10)
b.display()

o/p:
10->50->20->30->40->









 