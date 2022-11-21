from io import StringIO
import csv
import numpy as np
import math


def task(csvString):
    num_types = 5

    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    res = []
    for row in range(num_types):
        res.append(set())
    out = []
    for i in reader:
        out.append(i)
    gr = np.asarray(out)
    gr = gr.astype(int)

    nodes = []
    for i in gr:
        nodes.extend(i)
    nodes = list(set(nodes))
    nodes.sort()

    deep = []
    matrix = []
    paths = []
    for i in nodes:
        deep.append(0)
        matrix.append([])
        paths.append([])
        for j in nodes:
            matrix[i - 1].append(0)
        for k in range(5):
            paths[i - 1].append(0)
    for i in range(1, len(nodes)):
        paths[i][1] = 1
    for i in gr:
        matrix[i[0] - 1][i[1] - 1] = 1
    cur_branch = [0]
    while cur_branch != []:
        i = 0
        while i != len(matrix):
            if matrix[cur_branch[-1]][i] == 1:
                matrix[cur_branch[-1]][i] = 0
                cur_branch.append(i)
                break
            i += 1
        if i == len(matrix):
            deep[cur_branch[-1]] = len(cur_branch)
            for j in range(0, len(cur_branch) - 2):
                paths[cur_branch[j]][2] += 1
            if len(cur_branch) > 2:
                paths[cur_branch[-1]][3] += len(cur_branch) - 2

            if len(cur_branch) > 1:
                paths[cur_branch[-2]][0] += 1

            cur_branch.pop()

    dn = []
    for i in range(max(deep)):
        dn.append(deep.count(i + 1))

    for i in nodes:
        paths[i - 1][4] = dn[deep[i - 1] - 1] - 1

    gen = []
    for i in paths:
        gen.extend(i)
    gen_set = set(gen)
    gen_set.remove(0)
    H = 0
    for i in gen_set:
        H -= gen.count(i) * i / (len(nodes) - 1) * math.log(i / (len(nodes) - 1), 2)
    return H