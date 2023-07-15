import os 
import shutil

from_dir = "E:\White hat jr\Class-102"
to_dir = "E:\White hat jr\class102new"

listoffiles= os.listdir(from_dir)
#print(listoffiles)

for file_name in listoffiles:
    name, extension =os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension=="":
        continue
    if extension in [".gif",".png",".jpg",".jpeg",".jfif"]:
        path1= from_dir + "/" + file_name
        path2 = to_dir + "/" + "image_files"
        path3= to_dir + "/" + "image_files" + "/" + file_name
        #print("path1",path1)
        #print("path3",path3)

        if os.path.exists(path2):
            print("moving"+ file_name + "...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+ file_name + "...")
            shutil.move(path1,path3)