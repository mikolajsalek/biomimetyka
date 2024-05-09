import os
import imageio
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# gif z BAMY
images = []
'''
filenames = [os.path.join('BAMY', filename) for filename in os.listdir('BAMY')]

for filename in filenames:
    images.append(imageio.v2.imread(filename))

output = 'output.gif'

imageio.mimsave(output, images)
'''
# histogramy
output_folder = 'histogramy'
filenames_1 = [os.path.join('wybrane', filename) for filename in os.listdir('wybrane')]

for filename in filenames_1:
    image = Image.open(filename)
    gray_image = image.convert('L') # grayscale sie robi
    gray_array = np.array(gray_image)
    flat_array = gray_array.flatten()

    plt.hist(flat_array, bins=256, range=(0,255), density=True, color='gray', alpha=0.7)
    title = 'Histogram jasnosci obrazu' + filename
    plt.title(title)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    plot_path = os.path.join(output_folder, os.path.basename(filename) + '_histogram.png')
    plt.savefig(plot_path)
    plt.close()


