import matplotlib.pyplot as plt
import pyautogui as mouse
from collections import Counter as c
from scipy.ndimage.filters import gaussian_filter as gf
import numpy as np

file = open("mouse.re", "r")
file_lines = file.readlines()

positions = []
values = []
row = []

for line in file_lines:
    splot = [int(i) for i in line.split()]
    for _ in range(splot[2]):
        positions.append(tuple([splot[0], splot[1]]))

test = c(positions)

for x in range(mouse.size()[0]):
    for y in range(mouse.size()[1]):
        try:
            row.append(test[tuple([x, y])])
        except KeyError:
            row.append(0)
    values.append(row)
    row = []

values = np.array(values)
values = gf(values, sigma=10)

fig, ax = plt.subplots()
im = ax.imshow(values)
plt.show()
file.close()
