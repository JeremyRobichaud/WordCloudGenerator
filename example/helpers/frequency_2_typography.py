import os

from PIL import Image
from tqdm import tqdm
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np


def _get_frequency_paths():
    word_collection_txt_paths = []
    for file_name in os.listdir("./temp/frequency"):
        if not file_name.endswith(".txt"):
            continue
        file_path = os.path.join("./temp/frequency", file_name)
        word_collection_txt_paths.append(file_path)

    return word_collection_txt_paths


def _generate_frequency(frequency_path):
    frequency_dict = {}
    print("Loading " + frequency_path + "...")
    with tqdm(total=os.path.getsize(frequency_path)) as pbar:
        with open(frequency_path, 'r', encoding='utf-8') as infile:
            for line in infile:
                line_tokens = line.split(" ")
                frequency_dict[line_tokens[0]] = float(line_tokens[1].strip())
                pbar.update(len(line))

    return frequency_dict


def _get_background(img, inside, outside):
    pixels = img.load()
    for i in range(img.size[0]):  # for every pixel:
        for j in range(img.size[1]):
            if pixels[i, j] == (255, 255, 255):
                pixels[i, j] = inside
            else:
                pixels[i, j] = outside

    return img


def frequency_2_typography(mask_name, frequency_filename=None,
                           inside_color=None, inside_bg_color=None,
                           outside_color=None, outside_bg_color=None, outside_words=True):

    assert mask_name

    inside_color_mapping = {
        "colormap": inside_color or "brg"
    }
    if type(inside_color) == tuple:
        inside_color_mapping = {
            "color_func": lambda *args, **kwargs: inside_color
        }

    outside_color_mapping = {
        "colormap": outside_color or "brg"
    }
    if type(outside_color) == tuple:
        outside_color_mapping = {
            "color_func": lambda *args, **kwargs: outside_color
        }

    for frequency_path in _get_frequency_paths():
        if frequency_filename and frequency_path not in frequency_path:
            continue

        frequency_dict = _generate_frequency(frequency_path)

        print("Generating Image...")


        #  Colored text white Background
        i = Image.open(mask_name)
        mask = np.array(i)
        background = _get_background(i, inside_bg_color or (255, 255, 255), outside_bg_color or (255, 255, 255))
        inside_wordcloud = WordCloud(
            max_words=len(frequency_dict.keys()), mask=mask,
            background_color=None, mode="RGBA", **inside_color_mapping
        )

        inverse_mask = 255 - mask

        outside_wordcloud = WordCloud(
            background_color=None, mode="RGBA",
            max_words=len(frequency_dict.keys()), mask=inverse_mask,
            **outside_color_mapping
        )

        # Generate Words
        inside_wordcloud.generate_from_frequencies(frequency_dict)
        outside_wordcloud.generate_from_frequencies(frequency_dict)

        # show
        plt.imshow(background, interpolation="bilinear")
        plt.imshow(inside_wordcloud, interpolation='bilinear')
        if outside_words:
            plt.imshow(outside_wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
