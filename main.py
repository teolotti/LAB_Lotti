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
R = 1000000


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

    values = randomList(n, r)
    if not random:
        np.sort(values)
        if reversed:
            values = values[::-1]

    m = np.zeros((1, n))

    for p in range(1):
        for i, t in enumerate(values):
            start = timer()
            queue.insert(t)
            end = timer()
            m[p, i] = (end-start)

    return np.mean(m, 0)


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


def plot_generator(q_type, n, ins_test, ex_test, rand, style="", ord=False, rev=False, r=R):
    # heap se q_type == True, lista altrimenti
    # lista ordinata se ord == True, lista classica altrimenti
    # n: numero di elementi inseriti/estratti dalla coda
    # insert test se ins_test == True
    # extract test se ex_test == True
    # style == "o" per plot discreto + lettera per il colore
    # input randomizzato se rand == True, ordinato altrimenti
    # r: range dei numeri in input
    # input reversed (decrescente) se rev == True, crescente altrimenti

    q = createQueue(q_type, ord)
    it = insertTimeTest(n, q, rand, r, rev)
    print(it)  # per capire
    et = extractTimeTest(q)
    if ins_test:
        plt.plot(np.arange(n), it, style)  # "o" per plot discreto, altre lettere per colore
    if ex_test:
        plt.plot(np.arange(n), et, style)
    plt.xlabel("Numero di operazioni")
    plt.ylabel("Tempo(s)")


def main():
    # PRIMO TEST
    #plot_generator(True, 100, True, False, True)
    #plot_generator(False, 50, True, False, True)
    plot_generator(False, 50, True, False, True, "", True)

    # plt.xlabel--plt.ylabel--plt.title--plt.legend--plt.show

    plt.legend(["heap", "lista", "lista ord"])
    plt.show()


if __name__ == '__main__':
    main()
