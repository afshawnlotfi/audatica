from PIL import Image, ImageOps


class Mask:
    def __init__(self, mask_source, image_source, save_path):
        mask = Image.open(mask_source).convert('L')
        image = Image.open(image_source)
        output = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)
        output.save(save_path)
