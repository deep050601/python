import os
import shutil

print(os.getcwd())
os.chdir("D:\\CHROME DOWNLOADS")
print(os.getcwd())
all_files = os.listdir("D:\\CHROME DOWNLOADS")

if not "PDFS" in os.listdir():
    os.mkdir("PDFS")
if not "PHOTOS" in os.listdir():
    os.mkdir("PHOTOS")
if not "VIDEOS" in os.listdir():
    os.mkdir("VIDEOS")


for i in all_files:
    if i.endswith(".jpg"):
        shutil.move(i, "PHOTOS")
    elif i.endswith(".pdf"):
        shutil.move(i, "PDFS")
    elif i.endswith(".mkv"):
        shutil.move(i, "VIDEOS")
    elif i.endswith(".docx"):
        shutil.move(i, "PDFS")
    elif i.endswith(".png"):
        shutil.move(i, "PHOTOS")
    elif i.endswith(".mov"):
        shutil.move(i, "VIDEOS")
