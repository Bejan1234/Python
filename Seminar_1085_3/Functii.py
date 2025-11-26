import numpy as np


def random_AB(a, b, n):
    # functie care genereaza n valori aleatoare
    # in intervalul [A, B) din valori aleatori in [0, 1)
    return np.round(a + np.random.rand(n) * (b - a))