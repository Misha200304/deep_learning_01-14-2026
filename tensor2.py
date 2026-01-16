import torch
from  matrepr import mprint
import numpy as np

A = torch.tensor([
    [1,3],
    [5,2],
])

B = torch.tensor([
    [2,7],
    [10,1],
])

mprint(4*A)