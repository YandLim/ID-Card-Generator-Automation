# Importing Library
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import textwrap

# Define the path of the needed file
BLANK_ID = "data/Blank_ID.png"
CSV_FILE = "data/employees.csv"
FONT = "Fonts/Poppins/Poppins-Black.ttf"
RESULT = "Result"


# Resize the photo want to be pasted to fit perfectly into the spot
def resize_calculation(photo, top_left, bottom_right):
    target_width  = bottom_right[0] - top_left[0]
    target_height = bottom_right[1] - top_left[1]
    resize_image = photo.resize((target_width, target_height))
    return resize_image


# Adding text into the ID card
def add_text(im, font_size, text, top_left, bottom_right, color):
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(FONT, size=font_size) # Define the font to use
    wrapped_text = "\n".join(textwrap.wrap(text, width=15)) # Automatically wrap text onto multiple lines if it’s too long

    # Define the text box for accurate placement
    bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=font, align="center")
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    box_width = bottom_right[0] - top_left[0]
    box_height = bottom_right[1] - top_left[1]

    text_x = top_left[0] + (box_width - text_width) / 2
    text_y = top_left[1] + (box_height - text_height) / 2

    # Draw the text into the Image
    draw.multiline_text((text_x, text_y), wrapped_text, font=font, fill=color, align="center", spacing=5)
    return im


# Read the csv data file
df = pd.read_csv(CSV_FILE)

# Opening the Blank ID 
with Image.open(BLANK_ID) as blank:
    # Looping throught every row in the data
    for i, row in df.iterrows():
        # Opening the employe photo
        photo = Image.open(row["Photo"])

        # Resize the photo to fit into the space and paste into the blank ID card
        resize_photo = resize_calculation(photo.copy(), (238, 354), (785, 964))
        blank.paste(resize_photo, (238, 354))

        # Add name of the employee into the ID card
        add_text_im = add_text(blank.copy(), 80, row["Name"], (238, 1021), (786, 1115), (2,36,94))

        # Add ID of the employee into the ID card and save the final result 
        add_ID_im = add_text(add_text_im.copy(), 70, row["ID"], (238, 1175), (786, 1244), (2,36,94))
        add_ID_im.save(f"{RESULT}/ID_Card_{i}.png")
