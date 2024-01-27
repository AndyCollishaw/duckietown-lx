from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values

    
    res[400:, :40] =0.5
    res[360:, 40:80] = 0.5
    res[320:, 80:120] = 0.2
    res[280:, 120:160] = 0.2
    res[240:, 160:200] = 0.2
    res[160:, 200:240] = 0.5
    res[160:, 240:280] = 0.5
    res[160:200, 280:320] = 0.5

    
   

    
    # ---
    return res



def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    res[400:, 600:] = 0.5
    res[360:, 560:600] = 0.5
    res[320:, 520:560] = 0.2
    res[280:, 480:520] = 0.2
    res[240:, 440:480] = 0.5
    res[160:, 400:440] = 0.5
    res[160:, 360:400] = 0.5
    res[160:320, 320:360] = 0.5

    res[200:, 280:360] = 0.9
    
   
    
    # ---
    return res
