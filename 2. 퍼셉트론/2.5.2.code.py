import numpy as np

def basicgate(x1,x2,c):
    x = np.array([x1,x2])
    if c=='AND':
        w = np.array([0.5,0.5])
        b = -0.7
    elif c=='NAND':
        w = np.array([-0.5,-0.5])
        b = 0.7
    elif c=='OR':
        w = np.array([0.5,0.5])
        b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1,x2):
    s1 = basicgate(x1,x2,'NAND')
    s2 = basicgate(x1,x2,'OR')
    y = basicgate(s1,s2,'AND')
    return y

for i in range(2):
    for j in range(2): print(XOR(i,j))

# XOR gate의 경우 다층 퍼셉트론으로 구성 // gate 간 연결로 생각하면 쉽게 이해
# 입력(x1,x2)은 0층으로 생각 - 가중치를 갖는 층으로 퍼셉트론의 층수 고려