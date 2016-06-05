from PIL import ImageFilter, Image, ImageOps


class Blur():
    def __init__(self,image_source,save_path):
        image = Image.open(image_source)
        imageBlur=image.filter(ImageFilter.GaussianBlur(radius=100))
        imageBlur.save(save_path)

class Mask():
    def __init__(self,mask_source,image_source,save_path):

        mask=Image.open(mask_source).convert('L')
        image = Image.open(image_source)
        output=ImageOps.fit(image,mask.size,centering=(0.5,0.5))
        output.putalpha(mask)
        output.save(save_path)
