from PIL import Image
from os import listdir, path, remove

target_dir = "C:\\Users\\baris.kilinc\\Desktop\\Görsel\\HP"

target_size = (800, 800)

def resize_folder():
    for foldername in listdir(target_dir):
        print(foldername)
        count = 0
        for filename in listdir(f"{target_dir}\\{foldername}"):
            try:
                if filename[0:2] == "re":
                    continue
                # if filename.endswith(".asm") or filename.endswith(".py"): 
                image = Image.open(f"{target_dir}\\{foldername}\\{filename}")
                image = image.resize(target_size).convert("RGB")
                image.save(f"{target_dir}\\{foldername}\\re_{count}.jpg")
                count += 1
            except:
                print("ERROR working with file")
                print(f"{target_dir}\\{foldername}\\{filename}")

def delete_resised():
    for foldername in listdir(target_dir):
        for filename in listdir(f"{target_dir}\\{foldername}"):
            if filename[0:2] == "re":
                remove(f"{target_dir}\\{foldername}\\{filename}")

delete_resised()
resize_folder()