from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog

# create TKinter file dialog but first remove main dialog window
root = tk.Tk()
root.withdraw()
rootdir = filedialog.askdirectory()

# loop through root folder and sub directories. If .bmp files are found convert to .png and delete old files
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.lower().endswith('.bmp'):
            filepath = subdir + os.sep + file
            im = Image.open(filepath)
            im.save(os.path.splitext(filepath)[0] + '.png')
            os.remove(filepath)
