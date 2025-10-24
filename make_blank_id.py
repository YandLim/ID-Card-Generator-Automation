"""
This Python script converts a filled ID card into a blank template
by covering its contents with the card's background color.
"""

# Importing Library
from PIL import Image, ImageDraw

# Define the Card ID  
RAW_IMAGE = "data/Template_ID.png"

# Make the main function 
def cover_area(im, top_left, bottom_right, color):
    draw = ImageDraw.Draw(im)
    draw.rectangle((top_left, bottom_right), fill=color)
    return im

if __name__ == "__main__":
    with Image.open(RAW_IMAGE) as im:
        # Run the funtion and save the Blank ID
        rec_image = cover_area(im, (238, 354), (785, 1294), (245,244,244))
        rec_image.save("data/Blank_ID.png")
