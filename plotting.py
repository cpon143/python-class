import matplotlib.pyplot as plt
import numpy as np

xpts=np.array([0,6])
ypts=np.array([0,50])
plt.plot(xpts,ypts)
plt.show()
# ------------------------------------
# multiple line with style and single line
import matplotlib.pyplot as plt
import numpy as np
xpts=np.array([1,3,2,8])
ypts=np.array([6,1,8,10])
plt.plot(xpts,marker='*',ms=50,linestyle='dashed',mec='red')
plt.plot(ypts,marker='*',ms=50,mec='yellow',color='red',linewidth=10)
plt.show()

# Data about any company by grid graph

import matplotlib.pyplot as plt
import numpy as np
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

x1=np.array([0,1,2,3])
y1=np.array([1,8,2,7])
plt.plot(x1,y1)
plt.title('Data about xyz company')
plt.xlabel('x-axis',fontdict=font)
plt.ylabel('y-axis',fontdict=font)
plt.grid()
plt.show()

# ------------------Plotted graph-----------------------------

import matplotlib.pyplot as plt
import numpy as np
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

x1=np.array([0,1,2,3])
y1=np.array([1,6,5,7])
plt.subplot(1,2,1)
plt.plot(x1,y1)
x2=np.array([0,1,2,3])
y2=np.array([1,8,2,7])
plt.title('Data about abc company')
plt.xlabel('x-axis',fontdict=font)
plt.ylabel('y-axis',fontdict=font)
plt.grid()
plt.subplot(1,2,2)
plt.title('Data about xyz company')
plt.xlabel('x-axis',fontdict=font)
plt.ylabel('y-axis',fontdict=font)
plt.grid()
plt.plot(x2,y2)
plt.show()

# about two company data

import matplotlib.pyplot as plt
import numpy as np
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

x1=np.array([0,1,2,3])
y1=np.array([1,6,5,7])
plt.subplot(1,2,1)
plt.plot(x1,y1)
x2=np.array([0,1,2,3])
y2=np.array([1,8,2,7])
plt.title('BMW')
plt.xlabel('Years',fontdict=font)
plt.ylabel('Sold Cars',fontdict=font)
plt.grid()
plt.subplot(1,2,2)
plt.title('MARUTI')
plt.xlabel('Years',fontdict=font)
# plt.ylabel('y-axis',fontdict=font)
plt.grid()
plt.plot(x2,y2)
plt.show()