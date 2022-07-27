import numpy as np

def MMA(rpyt: list) -> np.array:
    if len(rpyt) != 4:
        raise TypeError

    r, p, y, t = rpyt

    return [
        t + r + p + y,
        t + r - p - y,
        t - r - p + y,
        t - r + p - y
    ]