import os
import threading
from time import time
import paddlehub as hub
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from alive_progress import alive_bar
from sqlalchemy import false, true


def cssColorString2list(string: str) -> list:
    '''
      输入一个css颜色字符串返回一个十进制数组
    '''
    out = []
    out.append(int(string[1:3], 16))
    out.append(int(string[3:5], 16))
    out.append(int(string[5:], 16))
    return out


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
path = input('图片所在文件夹：')

files = []

dirs = os.listdir(path)
for direction in dirs:
    files.append(path +'\\'+direction)

colorStr = input('切换背景色为(cssString):')
color = cssColorString2list(colorStr)

print('正在抠图:')
global results
# 3.抠图
calEnd=false

def printWait():
  timeStart = time()
  while calEnd:
    currentTime=time()
    str=['.' for i in range(np.math.floor(currentTime-timeStart)%12)]
  print(''.join(str),flush=true)

calThread = threading.Thread(target=printWait)
calThread.run()


results = humanSeg.segmentation(data={"image": files})
calEnd=true




with alive_bar(len(files)) as bar :

  for i, file in enumerate(files):

      img = mpimg.imread(file)

      human_range = results[i]['data']

      human_range = [[1 if cel > 0 else 0 for cel in row]for row in human_range]
      try:
        human_range=np.array(human_range).transpose()
        r = img[:, :, 0]*human_range
        g = img[:, :, 1]*human_range
        b = img[:, :, 2]*human_range
      except ValueError:
        human_range=np.array(human_range).transpose()
        r = img[:, :, 0]*human_range
        g = img[:, :, 1]*human_range
        b = img[:, :, 2]*human_range

      result = [[[r[i, j], g[i, j], b[i, j]] if r[i, j] > 0 else color for j in range(r.shape[1])]for i in range(r.shape[0])]

      # 展示预测结果图片
      result = np.array(result)

      plt.imshow(result)
      plt.axis('off')
      if not os.path.exists(path+'/output/'):
        os.mkdir(path+'/output/')
      plt.imsave(path+'/output/'+dirs[i], np.uint8(result))
      bar()
