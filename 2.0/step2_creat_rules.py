import numpy as np
import pickle


def find_poss(a, b, c):
    possibilities = {
        (0, 1, 1): 0.5,
        (1, 0, 1): 0.5,
        (0, 1, 0): 0.5,
        (1, 0, 0): 0.5,
        (1, 2, 1): 0.25,
        (2, 1, 1): 0.25,
        (1, 2, 2): 0.75,
        (2, 1, 2): 0.75,
        (1, 1, 0): 0.25,
        (1, 1, 2): 0.25,
        (1, 1, 1): 0.5,
        (2, 0, 1): 1,
        (0, 2, 1): 1,
        (0, 0, 0): 1,
        (2, 2, 2): 1
    }

    if (a, b, c) in possibilities:
        return possibilities[(a, b, c)]
    else:
        return 0


def adjust_poss(g1, g2, g3):
    poss = 1
    for i in range(len(g1)):
        poss *= find_poss(g1[i], g2[i], g3[i])
        if poss == 0:
            return 0
    return poss


def c():
    with open('population.pickle', 'rb') as f:
        p = pickle.load(f)

    arr = np.zeros((len(p), len(p), len(p)))

    for i in range(len(p)):
        for j in range(len(p)):
            for k in range(len(p)):
                arr[i][j][k] = adjust_poss(p[i], p[j], p[k])

    np.save('rules.npy', arr)


if __name__ == '__main__':
    print("sunoneeye")
