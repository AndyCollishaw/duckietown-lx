from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    #res[100:300, 0:320] = 0.3
    #res[301:, 50:400] = 0.8
    #res[301:, 400:590] = -1
    res[120:200, 160:320] = 0.1
    res[200:320, 160:320] = 0.3
    res[280:360, 80:280] = 0.3
    res[360:, 0:280] = 0.3
    res[280:, 280:360] = -1
    # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    #res[100:300, 321:] = 0.3
    #res[301:, 400:590] = 0.8
    #res[301:, 50:400] = -1
    res[120:200, 320:480] = 0.1
    res[200:400, 320:480] = 0.3
    res[280:400, 360:560] = 0.3
    res[360:, 360:] = 0.3
    res[280:, 280:360] = -0.8
    # ---
    return res
