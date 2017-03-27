from PIL import Image
from PIL import ImageFilter

Plaza = Image.open("Plaza Mayor.jpg")
blur = Plaza.filter(ImageFilter.BLUR)
detail = Plaza.filter(ImageFilter.DETAIL)
edges = Plaza.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()