


import torch
from . import _C


def forward(x):
    return _C.forward(x)