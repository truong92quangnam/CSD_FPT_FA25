#Mình nhắm đến là việc xử lý các trường hợp con trỏ nó sẽ trỏ như nào và cũng như là phải xử lý như nào cho thật tuần tựtự
class LinkedList:
    class Node:
        def __init__(self, data=None):
            self.data=data
            self.next=None
    
    def __init__(self):
        #Sẽ tạo initial của linked list gắn next của head là tail vì chưa có phần tử nào
        #Ý tưởng của mình là dùng near_last để nắm phần tử gần cuối để mình có thể trỏ vào tail
        #Vì đây là phần khởi tạo mình sẽ cho nó lấy ở phần tử head
        self.head=self.Node()
        self.tail=self.Node()
        self.head.next=self.tail

        self.__near_last=self.head
        self.__len=0
    
    def append(self, value):
        new_node=self.Node(value)
        if self.__len==0:
            self.head.next=new_node
            new_node.next=self.tail
            self.__near_last=new_node
            self.__len+=1
            return
        
        #Ở đây, sẽ xử lý theo ý tưởng near last sẽ là phần tử nắm đằng chuôi để gọi về vị trí của tail
        #Cũng có thể dùng ý tưởng này để dùng với khi len=0 
        self.__near_last.next=new_node
        self.__near_last.next.next=self.tail
        self.__near_last=new_node
        #----------------------------------------------------------Đây chính là tinh hoa---------------------------------------------
        self.__len+=1

    def traversal(self):
        curr=self.head
        while curr!=self.tail:
            print(curr.data, end='->')
            curr=curr.next
        print('None')
    
    def insert_by_position(self, position, value):
        #Nếu như nó đụng chạm đến vị trí của phần tử near_last thì mình cần phải thay đổi nó để follow kịp
        if position< self.__len:
            pos=-1
            curr=self.head
            while curr!=self.__near_last:
                if pos+1==position:
                    new_node=self.Node(value)
                    self.__len+=1
                    new_node.next=curr.next
                    curr.next=new_node
                    return 
                pos+=1
                curr=curr.next
        elif position==self.__len+1:
            self.append(value)
        else:
            print('Over the size')
    def insert_by_value(self, key, value):
        #Theo ý tưởng của mình thì với giá trị trong các box đấy thì nó sẽ không đụng chạm đến near_last nên mình sẽ không 
        #xử lý nó
        curr=self.head.next
        while curr!=self.tail:
            if curr.value==key:
                new_node=self.Node(value)
                self.__len+=1
                new_node.next=curr.next
                curr.next=new_node
                return  
            curr=curr.next
        print(f'{key} is not existed')
    
    def remove_by_position(self, position):
        #Đừng ông nào nghĩ là mình có thể remove 2 cái thằng head với tail nhá, vì nó là tuyệt đối rồi
        #Dĩ nhiên là nếu như đụng đến phần của near_last thì mình phải xử lý nó
        if position==self.__len-1:
            curr=self.head.next
            while curr.next !=self.__near_last:
                curr=curr.next
            #Đây chính là phần tinh hoa trong xử lý luồng này
            self.__near_last=curr
            self.__near_last.next=self.tail
            self.__len-=1
            return
        pos=-1
        curr=self.head
        while curr!=self.tail:
            if pos+1==position:
                curr.next=curr.next.next
                self.__len-=1
                return
            pos+=1
            curr=curr.next   
        print(f'{position} is not existed') 
    
    def remove_by_value(self, key):
        #y như thằng ở trên thôi nhưng sẽ sửa đổi một chút. Nếu như nó đụng được đến near_last thì mình còn có thể xử lý được
        if key==self.__near_last.data:
            curr=self.head.next
            while curr.next !=self.__near_last:
                curr=curr.next
            #Đây chính là phần tinh hoa trong xử lý luồng này
            self.__near_last=curr
            self.__near_last.next=self.tail
            self.__len-=1
            return
        curr=self.head
        while curr!=self.tail:
            if curr.next.data ==key :
                curr.next=curr.next.next
                self.__len-=1
                return
            curr=curr.next   
        print(f'{key} is not existed')

    def find(self, key):
        curr=self.head.next
        while curr!=self.tail:
            if key==curr.data:
                return 1
            else:
                return 0

def Main():

    Linked=LinkedList()
    Linked.append(1)
    Linked.append(2)
    Linked.append(3)
    Linked.append(4)
    Linked.remove_by_value(2)
    print(Linked.find(1))

Main()