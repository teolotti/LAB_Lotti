from math import*


class Heap:
    def __init__(self):
        self.size = 0
        self.A = []
        # Non considero la posizione 0 dell' array in nessun caso, rimarrà vuota

    def parent(self, i):
        return i // 2

    def left(self, i):
        return 2*i

    def right(self, i):
        return 2*i+1

    def swap(self, a, b):
        self.A[a], self.A[b] = self.A[b], self.A[a]

    def maxHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.size and self.A[l] >= self.A[i]:
            largest = l
        else:
            largest = i
        if r <= self.size and self.A[r] >= self.A[r]:
            largest = r
        if largest != i:
            self.swap(i, largest)
            self.maxHeapify(largest)

    def maximum(self):
        return self.A[1]

    def extractMax(self):
        temp = self.A[1]
        self.A[1] = self.A[self.size]
        self.size -= 1
        self.maxHeapify(1)
        return temp

    def insert(self, data):
        self.size += 1
        self.A[self.size] = data
        i = self.size
        while i > 1 and self.A[i] > self.A[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)




