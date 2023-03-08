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
        q = Heap()
    elif not ord:
        q = LinkedList()
    else:
        q = OrdLinkedList()
    return q


def insertTimeTest(n, queue, random, reversed=False):
    insertTime = []

    if random:
        list = randomList(n)
    elif not reversed:
        list = np.arange(n)
    else:
        list = np.arange(n)[::-1]


    for i in list:
        start = timer()
        queue.insert(i)
        end = timer()
        insertTime.append((end-start)/queue.size) #WHY

    for i in range(1,n):
        insertTime[i] += insertTime[i-1]

    return insertTime


def extractTimeTest(queue):
    n = queue.size
    extractTime = []

    for i in range(n):
        start = timer()
        queue.extractMax()
        end = timer()
        extractTime.insert(queue.size, (end - start)/(queue.size+1))

    for i in range(1,n):
        extractTime[i] += extractTime[i-1]

    return extractTime



def main():

    #PRIMO TEST
    qh = createQueue(True)
    ith = insertTimeTest(100, qh, True)
    eth = extractTimeTest(qh)
    plt.plot(np.arange(100), eth)


    ql = createQueue(False)
    itl = insertTimeTest(100, ql, True)
    etl = extractTimeTest(ql)
    plt.plot(np.arange(100), etl)


    qlo = createQueue(False, True)
    itlo = insertTimeTest(100, qlo, True)
    etlo = extractTimeTest(qlo)
    plt.plot(np.arange(100), etlo)

    plt.legend(['heap', 'list', 'ord_list'])
    plt.show()





if __name__ == '__main__':
    main()
