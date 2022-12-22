import json
import numpy as np
import pandas as pd

def yt(X, kt_1):
    return np.matmul(X, kt_1)

def kt(X, kt_1, s):
    lambtt = np.matmul(np.ones((len(s))), np.matmul(X,kt_1))
    return 1/lambtt*yt(X, kt_1)

def task(s):
    s = json.loads(s)
    obj_rang = np.zeros((len(s), len(s[0]), len(s[0])))
    #print(obj_rang)
    for i in range(len(s)):
        for j in range(len(s[0])):
            for k in range(len(s[0])):
                if s[i][j] > s[i][k]:
                    obj_rang[i][j][k] = 1
                elif s[i][j] == s[i][k]:
                    obj_rang[i][j][k] = 0.5
                else: obj_rang[i][j][k] = 0
    #print(obj_rang)
    X = np.zeros((len(s[0]), len(s[0])))

    for j in range(len(s[0])):
        for k in range(len(s[0])):
            for i in range(len(s)):
                X[j][k] += obj_rang[i][j][k]
    X = X/len(s)
    X = np.transpose(X)
    kt0 = np.ones((len(s)))/len(s)
    E = 10**(-3)
    while np.linalg.norm(kt(X, kt0, s) - kt0) >= E:
        kt0 = kt(X, kt0, s)
    res = list(np.around(kt(X, kt0, s), 3))
    encodedNumpyData = json.dumps(res)
    return encodedNumpyData


