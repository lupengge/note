import os
import sys
import paddlehub as hub
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
from PIL import Image

floor = math.floor

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

# 1.加载模型
humanSeg = hub.Module(name="deeplabv3p_xception65_humanseg")

# 2.指定待抠图图片目录
path = 'C:/Users/lpg/Desktop/testPyIMG/'
files = []
dirs = os.listdir(path)
for direction in dirs:
 files.append(path + direction)

# 3.抠图
results = humanSeg.segmentation(data={"image": files})


img = mpimg.imread(files[1])

human_range=results[1]['data']

human_range=[[1 if cel>0 else 0 for cel in row]for row in human_range]

r=img[:,:,0]*human_range
g=img[:,:,1]*human_range
b=img[:,:,2]*human_range

result=[[[r[i,j],g[i,j],b[i,j]] if r[i,j]>0 else [0,222,253] for i in range(r.shape[0])]for j in range(r.shape[1])]

bg=[[[255,0,0] if cel==0 else 0 for cel in row]for row in human_range]

# 展示预测结果图片
result=np.array(result)



plt.imshow(result)
plt.axis('off')
plt.show()
res = Image.fromarray(np.uint8(result))
res.save(path+'123121.png')
