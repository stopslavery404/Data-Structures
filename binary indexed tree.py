class BinaryIndexedTree:
    '''1 based indexing'''

    def __init__(self, arr):
        self.n = len(arr) + 1
        self.tree = [0 for i in range(self.n)]
        c = [0]
        for i in range(1, self.n):
            self.add(i, arr[i - 1])

    def getCumulativeFrequency(self, i):
        sum_ = 0
        while i > 0:
            sum_ += self.tree[i]
            i -= (i & -i)
        return sum_

    def add(self, i, val):
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def getFrequency(self, i):
        sum_ = self.tree[i]
        if i > 0:
            z = i - (i & -i)
            i -= 1
            while i != z:
                sum_ -= self.tree[i]
                i -= (i & -i)
        return sum_


arr = [1, 0, 2, 1, 1, 3, 0, 4, 2, 5, 2, 2, 3, 1, 0, 2]
t = BinaryIndexedTree(arr)
print(t.tree)
print(t.getCumulativeFrequency(16))
