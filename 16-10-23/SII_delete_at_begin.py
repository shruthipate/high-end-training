class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatend(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            curr=self.head
            while(curr.next):
                curr=curr.next
            new=Node(data)
            curr.next=new
    def deleteatbeg(self):
        if self.head==None:
            return
        temp=self.head
        self.head=self.head.next
        temp.next=None
        return temp.val
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
c=sll()
for i in l:
    c.insertatend(i)
print("The linked list is:")
c.printing()
print("Deleted Element:",c.deleteatbeg())
print("After Deleting at begin the list is:")
c.printing()