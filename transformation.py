from PIL import Image

tree = Image.open("Plaza Mayor.jpg")
square_tree = tree.resize((250, 250))
flip_tree = tree.transpose(Image.FLIP_LEFT_RIGHT)
spin_tree = tree.transpose(Image.ROTATE_90)

square_tree.show()
flip_tree.show()
spin_tree.show()