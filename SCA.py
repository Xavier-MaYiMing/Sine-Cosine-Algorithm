#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/8 14:41
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : SCA.py
# @Statement : Sine Cosine Algorithm
# @Reference : Mirjalili S. SCA: A Sine Cosine Algorithm for solving optimization problems[J]. Knowledge-Based Systems, 2016, 96.
import random
import math
import matplotlib.pyplot as plt


def obj(x):
    """
    The objective function of pressure vessel design
    :param x:
    :return:
    """
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    g1 = -x1 + 0.0193 * x3
    g2 = -x2 + 0.00954 * x3
    g3 = -math.pi * x3 ** 2 - 4 * math.pi * x3 ** 3 / 3 + 1296000
    g4 = x4 - 240
    if g1 <= 0 and g2 <= 0 and g3 <= 0 and g4 <= 0:
        return 0.6224 * x1 * x3 * x4 + 1.7781 * x2 * x3 ** 2 + 3.1661 * x1 ** 2 * x4 + 19.84 * x1 ** 2 * x3
    else:
        return 1e10


def boundary_check(value, lb, ub):
    """
    The boundary check
    :param value:
    :param lb: the lower bound (list)
    :param ub: the upper bound (list)
    :return:
    """
    for i in range(len(value)):
        value[i] = max(value[i], lb[i])
        value[i] = min(value[i], ub[i])
    return value


def main(pop, iter, lb, ub):
    """
    The main function of the SCA
    :param pop: the number of candidates
    :param iter: the iteration number
    :param lb: the lower bound (list)
    :param ub: the upper bound (list)
    :return:
    """
    # Step 1. Initialization
    a = 2  # a pre-defined parameter
    pos = []  # the position of all candidates
    score = []  # the score of all candidates
    dim = len(lb)  # dimension
    for i in range(pop):
        temp_pos = [random.uniform(lb[j], ub[j]) for j in range(dim)]
        pos.append(temp_pos)
        score.append(obj(temp_pos))
    iter_best = []
    gbest = min(score)  # the score of the best-so-far candidate
    gbest_pos = pos[score.index(gbest)].copy()  # the position of the best-so-far candidate
    iter_con = 0

    # Step 2. The main loop
    for t in range(iter):
        # Step 2.1. Calculate r1
        r1 = a - (t + 1) * a / iter

        # Step 2.2. Update positions
        for i in range(pop):
            for j in range(dim):
                r2 = random.uniform(0, 2 * math.pi)
                r3 = random.uniform(0, 2)
                r4 = random.random()
                if r4 < 0.5:
                    pos[i][j] += r1 * math.sin(r2) * abs(r3 * gbest_pos[j] - pos[i][j])
                else:
                    pos[i][j] += r1 * math.cos(r2) * abs(r3 * gbest_pos[j] - pos[i][j])
            pos[i] = boundary_check(pos[i], lb, ub)
            score[i] = obj(pos[i])

        # Step 2.3. Update the global best
        for i in range(pop):
            if score[i] < gbest:
                gbest = score[i]
                gbest_pos = pos[i].copy()
                iter_con = t + 1
        iter_best.append(gbest)

    # Step 3. Sort the results
    x = [i for i in range(iter)]
    plt.figure()
    plt.plot(x, iter_best, linewidth=2, color='blue')
    plt.xlabel('Iteration number')
    plt.ylabel('Global optimal value')
    plt.title('Convergence curve')
    plt.show()
    return {'best score': gbest, 'best solution': gbest_pos, 'convergence iteration': iter_con}


if __name__ == '__main__':
    # Parameter settings
    pop = 30
    iter = 1000
    lb = [0, 0, 10, 10]
    ub = [99, 99, 200, 200]
    print(main(pop, iter, lb, ub))
