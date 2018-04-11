#测试成功，但是origin文件夹消失
#思考后，因为renames是修改文件全名包含目录，所以源目录消失了
#当文件与目标文件夹冲突时，会有文件留在原文件夹，则不消失
#这其中就体现出与shutil的不同了
#文件转码有问题，部分错误命名有问题如S-cute
import os

path_old=  'H:\\seed\\2.番号\\封面中转\\暂存\\'
path_new=  'H:\\seed\\2.番号\\'
path_index='H:\\seed\\2.番号\\封面中转\\index.txt'
#初始化目录，视情况调用,
#def initial(pat):
#    pat=pat.strip().rstrip('\\')
#    return pat

result   =  os.walk(path_old)
for path_old, w, files in result:
    pass
#print(files)

with open(path_index,'a') as f:
    #覆盖写模式是w，续写模式是a
   for fi in files:
       fi=[''.join(fi)+'\n']
       try:
           f.writelines(fi)
       except UnicodeEncodeError:
           f.writelines('Encoding Error!!!!!!!!!')


for file in files:
    folder = file.split('-')
    folder = folder[0]+'\\'
    try:
        os.renames(path_old+file,path_new+folder.upper()+file)#大写文件夹
    except FileExistsError:
        print(file+ ' is Exists')


