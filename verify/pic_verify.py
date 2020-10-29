"""

简单图片验证码的识别
https://my.cnki.net/ 知网

PIL（Python Imaging Library Python，图像处理类库）提供了通用的图像处理功能，
以及大量有用的基本图像操作，比如图像缩放、裁剪、旋转、颜色转换等
"""

import tesserocr
from  PIL  import  Image
import os

"""
image=Image.open('CheckCode.jpg')
image = image.convert("L")#转化为灰度照片
image.show()

result=tesserocr.image_to_text(image)
result2=tesserocr.file_to_text('CheckCode.jpg')
print(result)
print(result2)
"""


"""批量图片格式转化"""

filelist=['CheckCode.jpg','timg.jpg']

for image_file in filelist:
    print(os.path)
    outfile=os.path.splitext(image_file)[0]+'.png'
    if image_file!=outfile:
        try:
            Image.open(image_file).convert('L').save(outfile)
        except IOError:
            print('转化失败',image_file)



