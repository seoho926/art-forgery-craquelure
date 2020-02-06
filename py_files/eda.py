"""Module with functions for making images grayscale and black & white"""
import cv2
from PIL import Image
import numpy as np
import os

def grayscale(file_name):
    """grayscaling image with 'file_name'"""
    image = cv2.imread(file_name, 0)
    cv2.imwrite('result.jpg', image) #to save as file
    cv2.imshow('result.jpg', image) #to open image in separate window
    cv2.waitKey(0) #enables window to open
    
def binarize_image(img_path, threshold):
    """Binarize an image - Making images black and white by changing 
    all pixels to 0 or 255 depending on whether the pixel value is 
    greater or less than the threshold"""
    image_file = Image.open(img_path)
    image = image_file.convert('L')  # convert image to monochrome
    image = np.array(image)
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] > threshold:
                image[i][j] = 255
            else:
                image[i][j] = 0
    return image

def invert_image(directory):
    """Inverting all black background and white line images separated 
    and gathered in a directory and resaving inverted version"""
    for filename in os.listdir(directory):
        im = Image.open(directory + filename).convert('RGB')
        im_invert = ImageOps.invert(im)
        im_invert.save(directory + filename)