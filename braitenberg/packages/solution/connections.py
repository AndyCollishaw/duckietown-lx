from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values

    res[400:, :40] = 1
    res[360:, 40:80] = 1
    res[320:, 80:120] = 1
    res[280:, 120:160] = 1
    res[240:, 160:200] = 1
    res[200:, 200:240] = 1
    res[160:, 240:280] = 1
    res[120:, 280:320] = 1

    res[400:, 600:] = -1
    res[360:, 560:600] = -1
    res[320:, 520:560] = -1
    res[280:, 480:520] = -1
    res[240:, 440:480] = -1
    res[200:, 400:440] = -1
    res[160:, 360:400] = -1
    res[120:, 320:360] = -1

    
    # ---
    return res



def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    res[400:, 600:] = 1
    res[360:, 560:600] = 1
    res[320:, 520:560] = 1
    res[280:, 480:520] = 1
    res[240:, 440:480] = 1
    res[200:, 400:440] = 1
    res[160:, 360:400] = 1
    res[120:, 320:360] = 1

    res[400:, :40] = -1
    res[360:, 40:80] = -1
    res[320:, 80:120] = -1
    res[280:, 120:160] = -1
    res[240:, 160:200] = -1
    res[200:, 200:240] = -1
    res[160:, 240:280] = -1
    res[120:, 280:320] = -1
    
    # ---
    return res
