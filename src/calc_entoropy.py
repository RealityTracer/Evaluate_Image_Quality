import cv2
import sys
import matplotlib.pyplot as plt
import numpy as np

args = sys.argv
if len(args) != 2:
    sys.exit()

def read_image(_img_name):
    # read input image
    img_BGR = cv2.imread(_img_name)

    # convert color (BGR → RGB)
    img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)

    return img_RGB

def calc_entropy(_histogram, _num_of_pixels):
    entropy = 0

    for i in range(256):
        p = _histogram[i]/_num_of_pixels
        if p == 0:
            continue
        entropy -= p*np.log2(p)

    return entropy

if __name__ == "__main__":
    # Read two input images
    img_in_RGB = read_image(args[1])

    # Convert RGB to Grayscale
    img_in_Gray = cv2.cvtColor(img_in_RGB, cv2.COLOR_RGB2GRAY)

    # Get histogram of the input image
    img_hist, img_bins = np.histogram(np.array(img_in_Gray).flatten(), bins=np.arange(256+1))
    # print(img_hist.shape) (255,)

    # Calculate entropy of the input image
    num_of_pixels = img_in_RGB.shape[0] * img_in_RGB.shape[1]
    entropy = calc_entropy(img_hist, num_of_pixels)
    print(f'Entropy: {entropy:.2f}')