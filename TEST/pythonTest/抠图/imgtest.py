import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import json

from numpy.lib.index_tricks import nd_grid

with open('./temp.json') as js:
  data=json.load(js)

human_range:np.array = np.array(data[0]['data'])
a=np.array(human_range)
print(a[0,0])

human_range=[[1 if cel>0 else 0 for cel in row]for row in human_range]

img = mpimg.imread('C:/Users/lpg/Desktop/testPyIMG/123.jpg')

r=img[:,:,0]*human_range
g=img[:,:,1]*human_range
b=img[:,:,2]*human_range

result=[[[r[i,j],g[i,j],b[i,j]]for i in range(r.shape[0])]for j in range(r.shape[1])]




print(result)
result=np.array(result)

plt.imshow(result)
plt.axis('off')
plt.show()
