import random

import numpy as np

from linked_list import *
from node import *
from ord_linked_list import *
from heap import *
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)
R = 1000000


def randomList(n, r):  # PROBLEMIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII GUARDA NOTEBOOK
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


def insertTimeTest(n, queue, random, r, reversed):
    values = randomList(n, r)
    if not random:
        values = np.sort(values)
        if reversed:
            values = values[::-1]

    it = []

    for t in values:
        start = timer()
        queue.insert(t)
        end = timer()
        it.append(end - start)

    return it


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


def plot_generator(q_type, n, ins_test, ex_test, rand, style="", ord=False, rev=False, r=R, num_t=200):
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
    mit = np.zeros((num_t, n))
    met = np.zeros((num_t, n))
    for p in range(num_t):
        it = insertTimeTest(n, q, rand, r, rev)
        et = extractTimeTest(q)
        mit[p, :] = it
        met[p, :] = et
    if ins_test:
        plt.plot(np.arange(n), np.mean(mit, 0), style)  # "o" per plot discreto, altre lettere per colore
    if ex_test:
        plt.plot(np.arange(n), np.mean(met, 0), style)
    plt.xlabel("Numero di operazioni")
    plt.ylabel("Tempo(s)")


def main():
    # PRIMO TEST
    plot_generator(True, 1000, True, False, False) #problemi su input random e reversed
    plot_generator(False, 100, True, False, False) #funziona insert
    plot_generator(False, 1000, True, False, False, "", True) #così funziona insert

    # plt.xlabel--plt.ylabel--plt.title--plt.legend--plt.show

    plt.legend(["heap", "lista", "lista ord"])
    plt.show()


if __name__ == '__main__':
    main()
