from PIL import Image

img = Image.open("Plaza Mayor.jpg")

area = (100, 100, 520, 620)
cropped_img = img.crop(area)
img.show()
cropped_img.show()