import pyautogui as mouse
from collections import Counter as c
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.filters import gaussian_filter as gf

sleep = float(input("Seconds per sample (<0.1s is recommended): "))
amount = int(input("Amount of samples: "))
agree = input("Are you sure? you will get " + str(sleep*amount) + "s of recording time (That's " + str(sleep*amount/60) + "m) (Y/n): ")
f = input("Would you like to save mouse replays? (Y/n): ")
recover = input("Would you like to recover replays? (Y/n): ")

if f != "n":
    try:
        file = open('mouse.re', "x")
        file.close()
        file = open('mouse.re', "r")
        file_lines = file.readlines()
        file.close()
        file = open('mouse.re', "r+")
    except FileExistsError:
        file = open('mouse.re', "r")
        file_lines = file.readlines()
        file = open('mouse.re', "r+")    


positions = []
a = 0

if agree.lower() == "n":
    quit()

while a <= amount:
    Fx, Fy = mouse.position()
    time.sleep(sleep)
    positions.append(tuple([Fx, Fy]))
    a += 1

for line in file_lines:
    splot = [int(i) for i in line.split()]
    for _ in range(splot[2]):
        positions.append(tuple([splot[0], splot[1]]))

test = c(positions)

file_addition = ""
if f != "n":
    for key in test.keys():
        file_addition = file_addition + str(key[0]) + " " + str(key[1]) + " " + str(test[key]) + "\n"
        file.write(file_addition)
        file_addition = ""

values = []
row = []

for x in range(mouse.size()[0]):
    for y in range(mouse.size()[1]):
        try:
            row.append(test[tuple([x, y])])
        except KeyError:
            row.append(0)
    values.append(row)
    row = []

# print(test)

values = np.array(values)
values = gf(values, sigma=10)

fig, ax = plt.subplots()
im = ax.imshow(values)
plt.show()
file.close()
