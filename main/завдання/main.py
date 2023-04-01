from PIL import Image, ImageFilter, ImageEnhance
with Image.open("original.jpg") as original:
    b_a_w = original.convert("L")
    blure_im = b_a_w.filter(ImageFilter.BLUR)
    rotate_im = blure_im.transpose(Image.Transpose.ROTATE_180)
    miror_im = original.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    pic_contrast = ImageEnhance.Contrast(original)
    pic_contrast = pic_contrast.enhance(1.5)

#открой файл с оригиналом картинки
original.show()
#орігінал дзеркально
miror_im.show()
#оригінал з більшим контрастом
pic_contrast.show()
#сделай оригинал изображения чёрно-белым
b_a_w.show()
#сделай оригинал изображения размытым
blure_im.show()
#поверни оригинал изображения на 180 градусов
rotate_im.show()