from PIL import ImageFilter, Image


class Blur:
    def __init__(self, image_source, save_path):
        image = Image.open(image_source)
        image_blur = image.filter(ImageFilter.GaussianBlur(radius=100))
        image_blur.save(save_path)
