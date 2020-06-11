#!/usr/bin/env python3

import numpy as np
import random
import time


def softmax(L):
    """
    Function that takes as input a list of numbers, and returns
    the list of values given by the softmax function.

    Arguments
    ---------

    L   :   list
            list with all the data


    Returns
    -------

    softmax_l applyed to all elements of the list

    """

    # avoid warning messages
    np.warnings.filterwarnings('ignore')

    # set decimal precision
    np.set_printoptions(9)

    start1 = time.time()
    numerator = np.exp(L - np.max(L))
    softmax = numerator / numerator.sum(axis=0)
    end1 = time.time()
    print("T1 (numpy) = {:.11f}".format(end1 - start1))

    start2 = time.time()
    expL = np.exp(L)
    sumExpL = sum(expL)
    result = []
    for i in expL:
        result.append(i * 1.0 / sumExpL)

    end2 = time.time()
    print("T2 (loops) = {:.11f}".format(end2 - start2))

    return softmax


for i in range (1, 8):
    n = pow(10, i)
    L = random.sample(range(0, n), n)
    print("Data = {}".format(n))
    s = softmax(L)
    print()
