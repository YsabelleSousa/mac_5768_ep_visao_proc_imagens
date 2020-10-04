from pathlib import Path
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from tqdm import tqdm

def return_folder_size_mb(path):

    root_directory = Path(path)
    return round(sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file()) / 1000000, 2)




def plot_images(path_data):
    lst_images = list()

    for root, subdirs, files in os.walk(os.path.abspath(path_data)):
        for file in files:
            if file.count('_') == 5:
                lst_images.append(root + '/' + file)

    plt.rcParams["figure.figsize"] = [16, 9]

    f, axarr = plt.subplots(9, 6)

    for i in tqdm(range(0, 9)):

        axarr[i, 0].imshow(mpimg.imread(random.sample(lst_images, 1)[0]))
        axarr[i, 1].imshow(mpimg.imread(random.sample(lst_images, 1)[0]))
        axarr[i, 2].imshow(mpimg.imread(random.sample(lst_images, 1)[0]))
        axarr[i, 3].imshow(mpimg.imread(random.sample(lst_images, 1)[0]))
        axarr[i, 4].imshow(mpimg.imread(random.sample(lst_images, 1)[0]))
        axarr[i, 5].imshow(mpimg.imread(random.sample(lst_images, 1)[0]))

    plt.show()