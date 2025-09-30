class ArrayQueue:
    def __init__(self, cap=5):
        self.Queue=[None]*cap
        self.firstIndex=-1
        self.length=0
        self.capacity=cap
    
    def isEmpty(self):
        return self.length==0
    
    def isFull(self):
        return self.length == self.capacity
    
    def increaseCapacity(self):
        lastindex= (self.firstIndex + self.length) % (self.capacity)
        curr=self.firstIndex
        pos=0
        new_Array=[None]*(self.capacity*2)
        while pos<self.length:
            curr=curr%self.capacity
            new_Array[pos]=self.Queue[curr]
            pos+=1
            curr+=1
        self.Queue=new_Array
        self.capacity*=2
        return new_Array

    def enqueue(self, val):
        if self.isEmpty():
            self.Queue[0]=val
            self.firstIndex=0
            self.length=1
            return
        if self.isFull():
            self.increaseCapacity()

        lastindex=(self.firstIndex+self.length)% self.capacity
        self.Queue[lastindex]=val
        self.length+=1
        pass

    def dequeue(self):
        if self.isEmpty():
            return
        self.Queue[self.firstIndex]=None
        self.firstIndex+=1
        self.firstIndex%=self.capacity
        self.length-=1
        return 
    
    def display(self):
        last_index= (self.firstIndex+self.length-1)% self.capacity
        curr=self.firstIndex
        while last_index+1!=curr:
            curr=curr%self.capacity
            print(self.Queue[curr], end=' ')
            curr+=1
        print()
        return 

if __name__=="__main__":
    queue=ArrayQueue()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(1)
    queue.display()

