import numpy as np

def relu(x):
    return np.maximum(0,x)
print(relu([-5.0,-3.0,1.0,5.0]))