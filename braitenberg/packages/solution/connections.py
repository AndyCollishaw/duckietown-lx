from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    #res[100:300, 0:320] = 0.3
    #res[301:, 50:400] = 0.8
    #res[301:, 400:590] = -1
    res[200:280, 80:320] = 0.3
    res[280:, :320] = 0.3
    res[200:480, 200:280] = 1
    # ---
    return res



def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    #res[100:300, 321:] = 0.3
    #res[301:, 400:590] = 0.8
    #res[301:, 50:400] = -1
    res[200:280, 320:560] = 0.3
    res[280:, 320:] = 0.3
    res[200:480, 360:440] = 1
    # ---
    return res
