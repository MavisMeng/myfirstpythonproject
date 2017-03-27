from PIL import Image

mayor = Image.open("Plaza Mayor copy.jpg")
plaza = Image.open("Plaza Mayor.jpg")

area = (100, 100, 220, 320)
mayor.paste(plaza, area)

mayor.show()