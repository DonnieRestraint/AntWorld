from PIL import Image

# 读取图片
im = Image.open(r"D:\images\img001.png")
# 展示图片
im.show()
# 打印图片信息
print(im.format, im.size, im.mode)
