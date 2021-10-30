import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,100,1000)
print(x)

plt.plot(x,x*x+x-x**3)
plt.show()
