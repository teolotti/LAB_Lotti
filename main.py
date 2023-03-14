import random

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
R = 5000


def randomList(n, r):
    a = []
    for i in range(n):
        el = random.randint(0, r)
        a.append(el)
    return a


def createQueue(heap, ord=False):
    if heap:
        q = Heap()
    elif not ord:
        q = LinkedList()
    else:
        q = OrdLinkedList()
    return q


def insertTimeTest(n, queue, random, r, reversed=False):
    insertTime = []

    values = randomList(n, r)
    if not random:
        np.sort(values)
        if reversed:
            values = values[::-1]

    for i in values:
        start = timer()
        queue.insert(i)
        end = timer()
        insertTime.append((end - start) / queue.size)  # WHY

    for i in range(1, n):
        insertTime[i] += insertTime[i - 1]

    return insertTime


def extractTimeTest(queue):
    n = queue.size
    extractTime = []

    for i in range(n):
        start = timer()
        queue.extractMax()
        end = timer()
        extractTime.insert(queue.size, (end - start) / (queue.size + 1))

    for i in range(1, n):
        extractTime[i] += extractTime[i - 1]

    return extractTime


def plot_generator(q_type, n, t_type, rand, ord=False, rev=False, r=R):
    # heap se q_type == True, lista altrimenti
    # lista ordinata se ord == True, lista classica altrimenti
    # n: numero di elementi inseriti/estratti dalla coda
    # insert test se t_type == True, extract test altrimenti
    # input randomizzato se rand == True, ordinato altrimenti
    # r: range dei numeri in input
    # input reversed (decrescente) se rev == True, crescente altrimenti

    q = createQueue(q_type, ord)
    it = insertTimeTest(n, q, rand, r, rev)
    et = extractTimeTest(q)
    if t_type:
        plt.plot(np.arange(n), it)
    else:
        plt.plot(np.arange(n), et)


def main():
    # PRIMO TEST
    plot_generator(False, 10000, True, True, True)

    # plt.xlabel--plt.ylabel--plt.title--plt.legend--plt.show

    plt.legend(['heap'])
    plt.show()


if __name__ == '__main__':
    main()
