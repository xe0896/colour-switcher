import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def process(data):
    # Locates zigzag.png in relative directory
    img = Image.open(data) 
    # Tranfsorms this into numpy array
    image_arr = np.array(img)
    # RGBA channel count, 4 implies RGBA
    channels = image_arr.shape[2]   

    if channels == 4:
        inverted_arr = 255 - image_arr[:,:,:3] # Inverts RGB channels
        inverted_arr = np.clip(inverted_arr, 0, 255) # Ensures values are in between 0 and 255
        inverted_arr = np.dstack([inverted_arr, image_arr[:,:,3]]) # Combines alpha channel with inverted array
    else:
        inverted_arr = 255 - image_arr # No need for alpha handling so we invert straight away
        inverted_arr = np.clip(inverted_arr, 0, 255)

    is_black = np.all(inverted_arr == [0,0,0,255], axis=-1) # Creates is-black mask which check if channel represents black, axis ensure individual checks
    inverted_arr[is_black] = [30, 30, 30, 255] # Applies mask to inverted array, this RGBA channel is the Obsidian color

    Image.fromarray(inverted_arr).save('output.png') # Saves inverted array as 'hello.png'

    plt.imshow(inverted_arr) # Prepares to show inverted array
    plt.show()  


