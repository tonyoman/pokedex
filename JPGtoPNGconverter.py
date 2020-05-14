import sys
import os  # grabs the path
from PIL import Image


# sys module - grab the first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]


# check if new/ exists and if not, create it
if not os.path.isdir(output_folder):
    os.makedirs(output_folder)

    # loop through pokedex,
    for image_file in os.listdir(image_folder):
        outfile = Image.open(f'{image_folder}{image_file}')
        # split filename from the extension and keep the filename
        clean_name = os.path.splitext(image_file)[0]
        # save images to the new folder
        # convert images to png
        # save images to the new folder
        outfile.save(f'{output_folder}{clean_name}.png', 'png')
        print('all done!')
