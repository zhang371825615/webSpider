"""
用于处理图片的工具类
"""


import os

#返回目录下所有图片
def get_image_list(path,endWith='.jpg'):
    #return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
    fileList=[]
    for f in os.listdir(path):
         if f.endswith(endWith):
             fileList.append(os.path.join(path,f))

    return fileList




print(get_image_list('d:\\198777\\Desktop\\'))
