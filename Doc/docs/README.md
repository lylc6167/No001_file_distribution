# No001_file_distribution




###1.输入原文件夹地址/a和目标文件夹地址/b

```
a='F:\xxx\xxx'
b='F:\xxx\xxx'
```
---
###2.使用os.walk()遍历读取/a中的文件，获取文件名列表A

```
import os
a=os.walk(a)
for q,w,e in a:
	print(e)
A=e
```

---
###3.使用正则获取番号，‘XXX-数字’模式，生成1级字典x={}，番号为key，全名为值
```
import re
p='.+-[0-9]{3,4,5}'#mxgs-1023,hodv-20213
a=re.findall(p,char)
```
或者考虑以'-'对列表每个元素进行划分，获得一个新列表后与元列表组成字典？（这种方法有一个问题，如果文件名头部有空格则无法操作

```
A=['xaax-123','aqwd-412','asg-1456','asd-231 1412']
i=0
B=[]
for a in A:
    b=a.split('-')
    B.append(b[0])
    i+=1
```
最终得到B列表为番号头部列表
---
###4.根据列表A、B，及python自带模块，将文件名对应文件剪切入/b中对应文件夹（字符串方法），如文件夹不存在则创建新文件夹
```
os.path.exists('')

```
---
###5.保存列表A到txt文件，以换行符做划分
---