import numpy as np

def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    """
    NAND gate
    w = np.array([-0.5,-0.5])
    b = 0.7
    
    OR gate
    w = np.array([0.5,0.5])
    b = -0.2
    """
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
for i in range(2):
    for j in range(2):
        print(AND(i,j))

# gate 구현은 가중치 w, 편향 b를 조절하여 가능