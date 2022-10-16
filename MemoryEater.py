import os,getpass

user = getpass.getuser()
directory = "C:/Users/"+user+"/Desktop/"

if os.path.isfile(directory+"inf.symbs"):
    os.remove(directory+"inf.symbs")
else:    
    file = open(directory+"inf.symbs","w")
    my_list = [0]
    for i in my_list:
        if i%20!=0:
            file.write("aboba")
            file.write(" | ")
            my_list.append(i+1)
        else: 
            file.write("aboba")
            file.write("\n")
            my_list.append(i+1)
    file.close()