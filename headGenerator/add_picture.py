# 图像叠加
# Date:2022/6/15
# LastEditDate:2022/6/19
# Author: Albert Wang
# E-mail: 13521713510@163.com

from PIL import Image
import base64

temp_path = r'D:\headGenerator\templates\temp\\'

def base64_to_jpg(img_name, base64data):
    data = base64.b64decode(base64data)
    # 生成图片
    file = open(temp_path + img_name + '.png', 'wb')
    file.write(data)


def draw_picture(base64data, img_name, rec_path, style):
    base64_to_jpg(img_name, base64data)  # 将base64数据转为png
    img = Image.open(temp_path + img_name + '.png')  # 打开图片
    img = img.convert('RGBA')  # 转为RGBA
    img_width, img_height = img.size  # 获取图片大小（像素）
    rec_image_path = rec_path + str(style) + ".png"  # 样式地址
    rec_image = Image.open(rec_image_path)  # 打开样式图片
    rec_image = rec_image.resize((img_width, img_height))  # 缩放（建议提交正方形图片以获得最佳体验）
    rec_image = rec_image.convert('RGBA')
    img_new = Image.alpha_composite(img, rec_image)  # 叠加图片
    img_new.save(temp_path + img_name + '_output.png')  # 生成叠加后图片
