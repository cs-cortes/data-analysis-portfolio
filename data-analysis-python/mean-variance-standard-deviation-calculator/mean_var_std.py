import numpy as np
import pandas as pd

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    a = np.array(list).reshape(3,3)
    b = a.flatten()

    stadictic = {
        'mean' : [a.mean(axis=0).tolist(), a.mean(axis=1).tolist(), float(b.mean())],
        'variance': [a.var(axis=0).tolist(), a.var(axis=1).tolist(), float(b.var())],
        'standard deviation': [a.std(axis=0).tolist(), a.std(axis=1).tolist(), float(b.std())],
        'max': [a.max(axis=0).tolist(), a.max(axis=1).tolist(), int(b.max())],
        'min': [a.min(axis=0).tolist(), a.min(axis=1).tolist(), int(b.min())],
        'sum': [a.sum(axis=0).tolist(), a.sum(axis=1).tolist(), int(b.sum())]
    }
    return stadictic



print(calculate(numbers))

