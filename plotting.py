import matplotlib.pyplot as plt
import numpy as np

xpts=np.array([0,6])
ypts=np.array([0,50])
plt.plot(xpts,ypts)
plt.show()

# multiple line with style and single line
import matplotlib.pyplot as plt
import numpy as np
xpts=np.array([1,3,2,8])
ypts=np.array([6,1,8,10])
plt.plot(xpts,marker='*',ms=50,linestyle='dashed',mec='red')
plt.plot(ypts,marker='*',ms=50,mec='yellow',color='red',linewidth=10)
plt.show()