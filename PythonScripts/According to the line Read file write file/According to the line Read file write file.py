# coding:utf-8
path = r"C:\Users\Administrator\Desktop\CSDN博客草稿\文件的读\password.txt"
#传入要读的文件路径
file = open("2007_train.txt","r",encoding="utf-8",errors="ignore")
"""
open表示打开你要执行的文件用读的方式打开
第一个参数是上面的文件path路径,第二个是所要执行的操作，（r）代表读，
#encoding="utf-8表示指定编码为“utf-8”，errors="ignore"表示读的时候遇到错误忽略
"""
f=open("path.txt", "a")#利用追加模式,参数从w替换为a即可
while True:
  mystr = file.readline()#表示一次读取一行
  mystr = mystr.split("/VOCdevkit/")
  print(mystr[0])
  f.write("./VOCdevkit/" + "{}".format(mystr[1]))
  if not mystr:
  #读到数据最后跳出，结束循环。数据的最后也就是读不到数据了，mystr为空的时候
    break
  print(mystr,end="")#打印每次读到的内容

