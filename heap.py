from math import*


class Heap:
    def __init__(self):
        self.size = 0
        self.A = []

    def parent(self, i):
        return floor(i/2)

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

    #TODO
    #build max heap(?), insert, maximum, extract max, increase key
