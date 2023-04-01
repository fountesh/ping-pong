from PIL import Image, ImageFilter 
with Image.open("фото редактор\Обои с темы.jpg") as original:
    new_image = original.convert("L")
    new_image = new_image.filter(ImageFilter.BLUR)
    new_image = new_image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    new_image = new_image.transpose(Image.Transpose.ROTATE_90)
    new_image.show()