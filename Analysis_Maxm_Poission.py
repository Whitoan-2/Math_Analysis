import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
start = 1
end = 10
m = np.linspace(start,end,end-start+1)
val = []
for e in m:
    x = np.linspace(e - 1, e, 100)
    y = np.exp(e) * np.exp(np.log(e) * x) / sp.special.gamma(x + 1)
    y2 = np.gradient(y, x)
    xt = x[1:]
    xint = xt[y2[1:] * y2[:-1] < 0]
    val.append(e-xint-0.5)
plt.plot(m,val)
plt.show()