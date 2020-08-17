class Deque:
    def __repr__(self):
        arr=[]
        for i in range(self.length):
            arr.append(self.popleft())
        for x in arr:
            self.append(x)
        return str(arr)

    def __init__(self, maxsize):
        self.length = 0
        self.maxsize = maxsize
        self.head = self.tail = 0
        self.arr = [None] * (self.maxsize)
        

    def appendleft(self, item):
        if self.full():
            raise OverflowError('queue is full')
        self.arr[self.tail] = item
        self.length+=1
        self.tail=(self.tail+1)%self.maxsize
        

    def pop(self):
        if self.empty():
            raise OverflowError('queue is empty')
        result = self.arr[self.head]
        self.arr[self.head] = None
        self.length-=1
        self.head =(self.head+1)%self.maxsize
        return result
    def append(self,item):
        if self.full():
            raise OverflowError('queue is full')
        self.head=(self.head-1)%self.maxsize
        self.arr[self.head]=item
        self.length+=1
    def popleft(self):
        if self.empty():
            raise OverflowError('queue is empty')
        self.tail=(self.tail-1)%self.maxsize
        result=self.arr[self.tail]
        self.arr[self.tail]=None
        
        self.length-=1
        return result
            

    def empty(self):
        return self.length==0

    def full(self):
        self.length==self.maxsize

    def front(self):
        if not self.empty():
            return self.arr[self.head]
    def end(self):
        if not self.empty():
            return self.arr[self.tail]


q = Deque(4)
print(q)
q.appendleft(4)
print(q)
q.append(5)
print(q)
q.appendleft(3)
print(q)
print(q.pop())
print(q)
print(q.popleft())
print(q)
q.append(5)
print(q)
q.appendleft(2)
print(q)