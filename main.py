from PIL import Image
from pillow_heif import register_heif_opener
import os
import tkinter as tk
from tkinter import filedialog as fd
from pathlib import Path
import time
from tqdm import tqdm

root = tk.Tk()
root.withdraw()
result = fd.askdirectory(
    master=root,
    mustexist=True
)
root.destroy()

if result:
    folder_path = f"{result}\\output"
    Path(folder_path).mkdir(parents=True, exist_ok=True)
    register_heif_opener()
    files = [file for file in os.listdir(result) if file.endswith('.HEIC') or file.endswith('.HEIF')]
    for filename in tqdm(files):
        time.sleep(0)
        image = Image.open(os.path.join(result, filename))
        image.convert('RGB').save(os.path.join(result, 'output', os.path.splitext(filename)[0] + '.jpg'))
else:
    exit()
