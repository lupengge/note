import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import json

from numpy.lib.index_tricks import nd_grid
from sqlalchemy import null

files = []
path = input('图片所在文件夹：')
dirs = os.listdir(path)


for direction in dirs:
    if os.path.isfile(os.path.join(path, direction)):
        files.append(path + '\\'+direction)
for (i,file) in enumerate(files):
  img = mpimg.imread(file)

  print(img.min())


  r=img[:,:,0]
  g=img[:,:,1]
  b=img[:,:,2]

  result=[[[0.,0.,0.,0.] if r[i,j]<70 and g[i,j]<70 and b[i,j]<70 else [r[i,j],g[i,j],b[i,j],255] for j in range(r.shape[0])]for i in range(r.shape[1])]



  result=np.array(result)

  if not os.path.exists(path+"/output"):
    os.mkdir(path+"/output")
  mpimg.imsave(path+'/output/'+dirs[i], np.uint8(result), format='png')
