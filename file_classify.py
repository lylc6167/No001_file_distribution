import os

path_old=  'F:\git\personal\\No001_file_distribution\\test\\origin\\'
path_new=  'F:\git\personal\\No001_file_distribution\\test\\target\\'

#初始化目录，视情况调用,
#def initial(pat):
#    pat=pat.strip().rstrip('\\')
#    return pat

result   =  os.walk(path_old)
for path_old, w, files in result:
    pass

print(files)

for file in files:
    folder = file.split('-')
    folder = folder[0]+'\\'
    os.renames(path_old+file,path_new+folder+file)