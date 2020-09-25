import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,5,0.01)

def f(x):
    phi=(1+np.sqrt(5))/2
    return ((phi**(x+0j))-((-1/phi)**(x+0j)))/np.sqrt(5)

y = f(x)
plt.plot(np.real(y),np.imag(y))
plt.show()
