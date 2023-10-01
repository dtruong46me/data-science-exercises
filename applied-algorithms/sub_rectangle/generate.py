from random import randint
import numpy as np

path = "applied-algorithms/sub-rectangle/data.txt"

def generate(n, m, white_rate):
    """
    n: row
    m: column
    white_rate: the percentage of white cell (0 < white_rate < 1)
    """
    white_cells = int(n * m * white_rate)

    white_cell_index = [randint(0, n*m) for _ in range(white_cells)]

    

    with open(path, 'w') as f:
        f.write(str(n) + str(m) + "\n")
