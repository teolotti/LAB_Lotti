import numpy as np

from linked_list import *
from node import *
from ord_linked_list import *
from heap import *
import numpy as num
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)
N = 100000

def randomList(n):
    a = np.arange(n)
    np.random.shuffle(a)
    return a


def createQueue(heap, ord=False):
    if heap:
        q = Heap(N)
    elif not ord:
        q = LinkedList()
    else:
        q = OrdLinkedList()
    return q


def insertTimeTest(n, queue, random, reversed=False):
    insertTime = [0]

    if random:
        list = randomList(n)
    elif not reversed:
        list = np.arange(n)
    else:
        list = np.arange(n)[::-1]

    count = 0
    for i in list:
        count += 1
        start = timer()
        queue.insert(i)
        end = timer()
        insertTime.append(((end-start)/queue.size) + insertTime[count-1]) #WHY

    return insertTime


def extractTimeTest(queue):
    extractTime = []

    for i in range(queue.get_size() + 1):
        start = timer()
        queue.extractMax()
        end = timer()
        extractTime.insert(queue.get_size()-i, round(end - start, 5)) #FIXME

    return extractTime


def main():

    #PRIMO TEST
    qh = createQueue(True)
    ith = insertTimeTest(10000, qh, True)
    plt.plot(np.arange(qh.size+1), ith)
    print(qh.A)


    ql = createQueue(False)
    itl = insertTimeTest(10000, ql, True)
    #plt.plot(np.arange(ql.size+1), itl)


    qlo = createQueue(False, True)
    itlo = insertTimeTest(1000, qlo, True)
    #plt.plot(np.arange(qlo.size+1), itlo)
    plt.show()





if __name__ == '__main__':
    main()
