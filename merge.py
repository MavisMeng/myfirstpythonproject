from PIL import Image

Plaza = Image.open("Plaza Mayor.jpg")
Mayor = Image.open("Plaza Mayor copy.jpg")

r1, g1, b1 = Plaza.split()
r2, g2, b2 = Mayor.split()

new_img = Image.merge("RGB", (r2, g1, b2))
new_img.show()