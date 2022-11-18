import json
import numpy as np
import pandas as pd
def task(s1, s2):
    s1 = json.loads(s1)
    s2 = json.loads(s2)
    obj1 = []
    obj2 = []
    s1_new = []
    s2_new = []
    for i in s1:
        if type(i) == list:
            for j in i:
                obj1.append(j)
            s1_new.append(i)
        else:
            obj1.append(i)
            s1_new.append([i])
    for i in s2:
        if type(i) == list:
            for j in i:
                obj2.append(j)
            s2_new.append(i)
        else:
            obj2.append(i)
            s2_new.append([i])

    A = np.zeros((len(obj1), len(obj1)))
    A = A.astype(int)
    B = np.zeros((len(obj2), len(obj2)))
    B = B.astype(int)
    A = pd.DataFrame(A, columns=obj1, index=obj1)
    B = pd.DataFrame(B, columns=obj1, index=obj1)

    prev = []
    for i in s1_new:
        prev.extend(i)
        for k in i:
            for j in prev:
                A.loc[j][k] = 1
    prev = []
    for i in s2_new:
        prev.extend(i)
        for k in i:
            for j in prev:
                B.loc[j][k] = 1
    At = A.transpose()
    Bt = B.transpose()
    mul = A.mul(B, 1)
    mul_t = At.mul(Bt, 1)
    res = []
    for i in obj1:
        for j in obj1:
            if mul[i][j] == 0 and mul_t[i][j] == 0:
                res.append([i, j])
    return res[:len(res)//2]





