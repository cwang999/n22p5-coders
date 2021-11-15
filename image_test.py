# Import required Image library
from PIL import Image, ImageDraw, ImageFont

# Create an Image Object from an Image
im = Image.open('./templates/about_page_pictures/IMG-6667.JPG')

# show 270 degree flipped image
degree_flippedImage = im.transpose(Image.ROTATE_270)
degree_flippedImage.show()

width, height = degree_flippedImage.size

draw = ImageDraw.Draw(degree_flippedImage)
text = "Del Norte High School"

font = ImageFont.truetype('arial.ttf', 96)
textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
margin = 100
x = width - textwidth - margin
y = height - textheight - margin*29

# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)
degree_flippedImage.show()

# Save watermarked image
degree_flippedImage.save('./static/assets/Davidwatermark.jpg')

