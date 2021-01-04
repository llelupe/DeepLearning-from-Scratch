import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x>0,dtype=np.int)

x=np.arange(-5.0,5.0,0.1) # -5.0~5.0 범위 0.1 단위 배열 생성
y=step_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1) # y축의 범위 지정
plt.show()