import cv2
import numpy as np
from PIL import Image

n = int(input("Топ цветов: "))
str = input("File name: ")
image = cv2.imread(str)

colors, counts = np.unique(image.reshape(-1, 3), axis=0, return_counts=True)
colors = list(colors)
counts = list(counts)
list_im = []
for i in range (n):
    idx = counts.index(max(counts))
    print(colors[idx], counts[idx])
    img = Image.new('RGB', (300, 200), (colors[idx][2], colors[idx][1], colors[idx][0]))
    list_im.append(img)
    counts.pop(idx)
    colors.pop(idx)

widths, heights = zip(*(i.size for i in list_im))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in list_im:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('colours.jpg')
