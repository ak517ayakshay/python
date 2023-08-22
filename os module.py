import os
# print(dir(os))
# os.mkdir("data")
# this created a directory name data1
# this is very good module u need to explore it, it can do evrything to ur os add rename delete etc
# for i in range(1,100):
    # os.mkdir(f"data{i}")
# this created 100 folders
# for i in range(1,100):
    # os.rename(f"data{i}",f"tutorial{i}")
    # this renames all the folders to tutorial
os.listdir("tutorial1")
# this lists all the folders present in tht folder
for i in range(1,100):
     os.rmdir(f"tutorial{i}")
    #  removes the dir which is empty
