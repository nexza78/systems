from io import StringIO
import csv
import numpy as np


def task1(csvString):
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

    for i in gr:
        res[0].add(i[0])
        res[1].add(i[1])

    size = gr.shape[0]
    for i in range(size):
        compare_el = gr[i][1]
        next_node = set()
        next_node.add(compare_el)
        while next_node != set():
            next_node.clear()
            for j in range(i+1, size):
                if compare_el == gr[j][0]:
                    next_node.add(gr[j][1])
                    res[2].add(gr[i][0])
                    res[3].add(gr[j][1])
            if next_node != set():
                compare_el = next_node.pop()
    compare_el = 1
    cur_neighbours = set()
    cur_neighbours.add(compare_el)
    checked = set()
    for i in range(size):
        if gr[i][0] in checked:
            continue
        cur_neighbours = set()
        compare_el = gr[i][0]
        next_node = set()
        next_node.add(compare_el)
        while next_node != set():
            next_node.clear()
            for j in range(i, size):
                if compare_el == gr[j][0]:
                    cur_neighbours.add(gr[j][1])

            if next_node != set():
                compare_el = next_node.pop()
        if len(cur_neighbours) > 1:
            for t in cur_neighbours:
                res[4].add(t)
        next_node = cur_neighbours
        cur_neighbours.clear()
        compare_el = gr[i][1]
    for i in range(len(res)):
        res[i] = list(res[i])
        res[i].sort()
    return res




