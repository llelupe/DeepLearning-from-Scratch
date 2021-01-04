def step_function(x):
    if x>0:
        return 1
    else:
        return 0
# 인수 x는 실수만 가능

def step_func(x):
    y = x>0 # y는 원소의 조건에 따른 bool형 배열
    return y.astype(np.int) # bool형 배열을 True=1/False=0으로 return
# 인수 x가 배열 가능

import numpy as np
x=np.array([-1.0,1.0,2.0])
print(step_func(x))