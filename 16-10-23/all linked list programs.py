'''class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
o1=node(1)
o2=node(2)
o3=node(3)
o1.next=o2
o2.next=o3
print(o1,o1.val,o1.next)
print(o1,o2.val,o2.next)
print(o1,o3.val,o3.next)'''
'''
class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val)
            temp=temp.next
            
l=[2,4,6,8]
c=sll()
for i in l:
    c.insertatbeg(i)
c.printing()'''




'''
class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbegin(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            new=Node(data)
            new.next=self.head
            self.head=new
    def insertatend(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            curr=self.head
            while(curr.next):
                curr=curr.next
            new=Node(data)
            curr.next=new
    def deleteatbegin(self):
        if self.head==None:
            return
        temp=self.head
        self.head=self.head.next
        temp.next=None
        return temp.val
    def deleteatend(self):
        if self.head==None:
            return
        temp=self.head
        while(temp.next.next):
            temp=temp.next
        temp.next=None
    
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
c=sll()
for i in l:
     c.insertatbegin(i)
     #c.insertatend(i)
print("Deleted Element:",c.deleteatend())
print("After Deleting at end the list is:")
c.printing()'''

'''#insert at begin for doubly
class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.prev=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val)
            temp=temp.next
            
l=[2,4,6,8]
c=dll()
for i in l:
    c.insertatbeg(i)
c.printing()'''
'''
#insertatend for doubly
class Node:
    def __init__(self,val=0):
        self.prev=None
        self.val=val
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def insertatend(self,data):
        if self.head==None:
            self.head=Node(data)
            self.tail=self.head
        else:
            new=Node(data)
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
c=dll()
for i in l:
    c.insertatend(i)
print("The linked list is:")
c.printing()'''

'''
#delete at begin
class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
    def insertatend(self,data):
        if self.head==None:
            self.head=Node(data)
            self.tail=self.head
        else:
            new=Node(data)
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
    def deleteatbeg(self):
        if self.head==None:
            return
        self.head=self.head.next
        self.head.prev=None
    
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
c=dll()
for i in l:
    c.insertatend(i)
print("The linked list is:")
c.deleteatbeg()
print("After deleting at begin the linked list is:")
c.printing()'''
'''
#delete at end
class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
    def insertatend(self,data):
        if self.head==None:
            self.head=Node(data)
            self.tail=self.head
        else:
            new=Node(data)
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
    def deleteatend(self):
        if self.head==None:
            return
        self.tail=self.tail.prev
        self.tail.next=None
    
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
c=dll()
for i in l:
    c.insertatend(i)
print("The linked list is:")
c.printing()
c.deleteatend()
print("After Deleting at end the list is:")
c.printing()'''

#reverse

class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
    def insertatend(self,data):
        if self.head==None:
            self.head=Node(data)
            self.tail=self.head
        else:
            new=Node(data)
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
    def deleteatend(self):
        if self.head==None:
            return
        self.tail=self.tail.prev
        self.tail.next=None
    def reverse(self):
        temp=self.tail
        while(temp):
            print(temp.val)
            temp=temp.prev
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
c=dll()
for i in l:
    c.insertatend(i)
print("The linked list is:")
c.printing()
print("reverse list is")
c.reverse()





