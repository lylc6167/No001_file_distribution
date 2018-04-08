import os
a= os.walk('H:\seed\\2.番号\封面中转')
for q,w,e in a:
    print(e)

A=['xaax-123','aqwd-412','asg-1456','asd-231 1412','asd-123 鸟酱']
i=0
B=[]
for a in A:
    b=a.split('-')
    B.append(b[0])
    i+=1
#从这步开始可以获取到A、B两个列表，可根据单个元素直接操作

C={}
i=0
for b in B:
    C[B[i]]=A[i]
    i+=1