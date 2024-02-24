import os
import shutil

from_dir="C:/Users/MY PC/Documents"
to_dir="C:/Users/MY PC/Downloads"
list_of_file=os.listdir(from_dir)
print(list_of_file)
for file_name in list_of_file:
    name,extention = os.path.splitext(file_name)
    print(name)
    print(extention)
    
    if extention=="":
        continue
    if extention in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Image_Files"
        path3 = to_dir + '/' + "Image_Files" + '/' + file_name
        
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)