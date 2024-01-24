from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values

    res[0:240, 320:] = 0.1
    res[240:, :320] = 0.5
    res[320:, 320:] = -0.4
    # ---
    return res



def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    res[0:240, 0:320] = 0.1
    res[240:, 320:] = 0.5
    res[320:, :320] = -0.4
    # ---
    return res
