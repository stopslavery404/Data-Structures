class Stack:
    '''
    Stack is a linear data structure in which
    insert and delete operations are performed
    in constant time.

    It follows Last In First Out (LIFO)
    the element which is inserted last is the
    element which exits first.



    Time complexity
    push->      O(1)
    pop->       O(1)
    top->       O(1)
    isEmpty->   O(1)
    '''

    def __init__(self, maxsize):
        '''creates stack of max capacity maxsize'''
        self.__top = -1
        self.__arr = [0] * maxsize
        self.maxsize = maxsize

    def isEmpty(self):
        '''returns True if stack is empty'''
        return self.__top == -1

    def push(self, item):
        '''push an item into the stack
        example push(item)'''
        if self.__top == self.maxsize - 1:
            raise StackOverflow("Stack is full, can't push items.")
        self.__top += 1
        self.__arr[self.__top] = item

    def pop(self):
        '''returns the top element and removes it from stack'''
        if self.isEmpty():
            raise StackUnderflow("Stack is empty, nothing to pop.")
        self.__top -= 1
        return self.__arr[self.__top + 1]

    def top(self):
        '''returns the top element without removing'''
        if self.__top == -1:
            raise StackUnderflow('stack is empty')
        return self.__arr[self.__top]

    def __len__(self):
        return self.__top + 1


class StackOverflow(Exception):
    pass


class StackUnderflow(Exception):
    pass
