class DoubleLinkedList:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data=data
            self.prev=prev
            self.next=next
    
    def __init__(self):
        self.head= self.Node()
        self.tail= self.Node()

        self.head.next=self.tail
        self.tail.prev=self.head
        self.__size=0
    
    def append(self, value):
        new_node = self.Node(value)

        self.tail.prev.next = new_node
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        self.tail.prev = new_node

        self.__size += 1
    
    def appfront(self, value):
        new_node= self.Node(value)
        next_node= self.head.next

        new_node.prev= self.head
        next_node.prev=new_node

        self.head.next = new_node
        new_node.next=next_node

        self.__size+=1

    def print_list(self):
        current = self.head.next
        while current != self.tail:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
    
    def len(self):
        return self.__size
    
    def print_list_reverse(self):
        curr= self.tail.prev
        while curr != self.head:
            print(curr.data, end=' <-> ')
            curr=curr.prev
        print('None')
    def insert_by_key(self, key, value):
        new_node=self.Node(value)
        curr = self.head.next
        while curr!=self.tail:
            if curr.data==key:
                next_node = curr.next
                next_node.prev=new_node
                new_node.prev=curr

                curr.next=new_node
                new_node.next=next_node
                self.__size+=1
                return
            curr=curr.next
    
    def insert_by_position(self, positon, value):
        if positon>self.__size:
            return
        new_node=self.Node(value)
        curr = self.head
        pos=0
        while curr!=self.tail:
            if pos==positon:
                next_node = curr.next
                next_node.prev=new_node
                new_node.prev=curr

                curr.next=new_node
                new_node.next=next_node
                self.__size+=1
                return
            curr=curr.next
            pos+=1
    def pop(self):
        if self.__size==0:
            return
        prev_node=self.tail.prev.prev
        prev_node.next=self.tail
        self.tail.prev=prev_node
        self.__size-=1
    
#Ở các phần mà được dùng để gán vào thì mình sẽ xử lý theo prev trước 
#rồi mới qua next hoặc ngược lại đều được vì vậy sẽ làm tránh nhầm lẫn để rồi gây
#ra lộn xộn
def Main():
    linkedlist=DoubleLinkedList()
    linkedlist.append(1)
    linkedlist.append(2)
    linkedlist.append(4)
    linkedlist.insert_by_key(2, 3)
    linkedlist.insert_by_position(0,10)
    linkedlist.pop()
    linkedlist.print_list()
Main()
