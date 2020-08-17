class Queue:
    def __repr__(self):
        return str(self.arr) + 'head={}, tail={}'.format(self.head, self.tail)

    def __init__(self, maxsize):
        self.length = 0
        self.maxsize = maxsize
        self.head = self.tail = 0
        self.arr = [None] * (self.maxsize)

    def enqueue(self, item):
        if self.length == self.maxsize:
            raise Error("Overflow")
        self.arr[self.tail] = item
        self.length += 1
        self.tail = (self.tail + 1) % self.maxsize

    def dequeue(self):
        if self.length == 0:
            raise Error("dequeue from empty queue.")
        result = self.arr[self.head]
        self.arr[self.head] = None
        self.length -= 1
        self.head = (self.head + 1) % self.maxsize
        return result

    def empty(self):
        return self.length == 0

    def full(self):
        self.length == self.maxsize

    def front(self):
        if not self.empty():
            return self.arr[self.head]


class Error(Exception):
    pass


q = Queue(4)
print(q)
for x in ['a', 'b', 'c', 'd']:
    q.enqueue(x)
    print(q)
for i in range(4):
    print(q.dequeue())
    print(q)
