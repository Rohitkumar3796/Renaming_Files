import os
path = os.chdir("path")# here have to give path where the images or filees is stored
a=0
for file in os.listdir(path): #to use listdir to return the list of any type of file name it will show
    #here we will use format function
    # the old name of file is img0 to img13
    new_name = 'pic{}.jpg'.format(a)
    # the new name you can check
    os.rename(file,new_name)
    a=a+1