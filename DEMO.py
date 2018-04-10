import os
a= os.walk('H:\seed\\2.番号\封面中转')
#os.walk会遍历所有子目录，所以当父目录下含有子目录时，
# e最终会显示为最后一个遍历到的文件夹
for q,w,A in a:
    print(A)
#q为完全地址，全部为双斜杠,可以使用

A=['xaax-123.jpg','aqwd-412.jpg','asg-1456.jpg','asd-231 1412.jpg','asd-123 鸟酱.jpg']
i=0
B=[]
for a in A:
    b=a.split('-')
    B.append(b[0])
    i+=1
#从这步开始可以获取到A、B两个列表，可根据单个元素直接操作
#正式程序中可以在一个循环中完成全部动作
path_from='F:\git\personal\\No001_file_distribution\\test\\origin'
path_to='F:\git\personal\\No001_file_distribution\\test\\target'
def initial(pat):
    pat=pat.strip().rstrip('\\')
    return pat
#使用initial(path)去除头部空格和尾部'\\'
i=0
for b in B:
    path_to_son=initial(path_to)+'\\'+b
    isExists=os.path.exists(path_to_son)
    if not isExists:
        os.mkdir(path_to_son)
        #不存在则创建
    else:
        pass
        #存在则pass
    os.rename(path_from+'\\'+A[i],path_to_son+'\\'+A[i])
    #使用os.renames()可以跳过判断步骤





#C={}
#i=0
#for b in B:
#    C[B[i]]=A[i]
#    i+=1