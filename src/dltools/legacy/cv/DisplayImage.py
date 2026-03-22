import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

class DisplayImage:
    def __init__(self, image_paths, titles, axis_off=True):
        """
        Initializes the DisplayImage class with image paths and titles.

        Parameters:
        - image_paths: List of paths to the images.
        - titles: List of titles for each image.
        - axis_off: Boolean indicating whether to turn off the axis.
        """
        self.image_paths = image_paths
        self.titles = titles
        self.axis_off = axis_off

    def byGrid2x2(self):
        """
        Displays images in a 2x2 grid with titles.
        """
        fig, axs = plt.subplots(2, 2)

        for i in range(2):
            for j in range(2):
                img_index = i * 2 + j
                axs[i, j].imshow(np.array(Image.open(self.image_paths[img_index])))
                axs[i, j].set_title(self.titles[img_index], y=-0.2)
                if self.axis_off:
                    axs[i, j].axis('off')

        plt.tight_layout()
        plt.show()

# Example usage
# image_paths = ["./data/model_1.png", "./data/model_2.png", "./data/model_3.png", "./data/model_4.png"]
# titles = ["Homo.SO", "Homo.MO", "Hetero.SO", "Hetero.MO"]
# display_image = DisplayImage(image_paths, titles)
# display_image.display()
