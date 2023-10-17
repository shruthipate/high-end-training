'''class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class cll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=Node(data)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            new=Node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
            self.tail.next=self.head
            self.head.prev=self.tail
    def printing(self):
        print(self.head.val)
        temp=self.head.next
        while(temp!=self.head):
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
c=cll()
for i in l:
    c.insertatbeg(i)
print("The linked list is:")
c.printing()'''
'''
#insert at end
class Node:
    def __init__(self,val=0):
        self.prev=None
        self.val=val
        self.next=None
class cll:
    def __init__(self):
        self.head=None
    def insertatend(self,data):
        if self.head==None:
            self.head=Node(data)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            new=Node(data)
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
            self.tail.next=self.head
            self.head.prev=self.tail
    def printing(self):
        print(self.head.val)
        temp=self.head.next
        while(temp!=self.head):
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
c=cll()
for i in l:
    c.insertatend(i)
print("The linked list is:")
c.printing()'''
'''
#delete begin
class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class cll:
    def __init__(self):
        self.head=None
    def insertatend(self,data):
        if self.head==None:
            self.head=Node(data)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            new=Node(data)
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
            self.tail.next=self.head
            self.head.prev=self.tail
    def deleteatbeg(self):
        if self.head==None:
            return
        self.head=self.head.next
        self.tail.next=self.head
        self.head.prev=self.tail
    def printing(self):
        print(self.head.val)
        temp=self.head.next
        while(temp!=self.head):
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
c=cll()
for i in l:
    c.insertatend(i)
print("The linked list is:")
c.printing()
c.deleteatbeg()
print("After deleting at begin the linked list is:")
c.printing()

'''
#delete end
class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class cll:
    def __init__(self):
        self.head=None
    def insertatend(self,data):
        if self.head==None:
            self.head=Node(data)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            new=Node(data)
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
            self.tail.next=self.head
            self.head.prev=self.tail
    def deleteatend(self):
        if self.head==None:
            return
        self.tail=self.tail.prev
        self.tail.next=self.head
        self.head.prev=self.tail
    def printing(self):
        print(self.head.val)
        temp=self.head.next
        while(temp!=self.head):
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
c=cll()
for i in l:
    c.insertatend(i)
print("The linked list is:")
c.printing()
c.deleteatend()
print("After deleting at end the linked list is:")
c.printing()

