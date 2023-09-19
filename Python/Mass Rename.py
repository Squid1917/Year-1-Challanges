import os;
folder = input("Enter Folder Path: ")


for count, filename in enumerate(os.listdir(folder)):

    if count < 10:
        dst = f"Lego Ninjago - S1{folder[len(folder) - 1]}E0{str(count + 1)}.mp4"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
            
        # rename() function will
        # rename all the files
        os.rename(src, dst)

    else:
        dst = f"Lego Ninjago - S1{folder[len(folder) - 1]}E{str(count + 1)}.mp4"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
            
        # rename() function will
        # rename all the files
        os.rename(src, dst)
        