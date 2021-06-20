#!/usr/bin/env python3
# coding: utf-8

# 解压tar.gz文件
import os, tarfile

def untar(fname, dirs):
    """
    解压tar.gz文件
    :param fname: 压缩文件名
    :param dirs: 解压后的存放路径
    :return: bool
    """
    try:
        t = tarfile.open(fname)
        t.extractall(path = dirs)
        return True
    except Exception as e:
        print(e)
        return False

untar('Annotations.rar','./')


# 解压zip文件
import zipfile

'''
基本格式：zipfile.ZipFile(filename[,mode[,compression[,allowZip64]]])
mode：可选 r,w,a 代表不同的打开文件的方式；r 只读；w 重写；a 添加
compression：指出这个 zipfile 用什么压缩方法，默认是 ZIP_STORED，另一种选择是 ZIP_DEFLATED；
allowZip64：bool型变量，当设置为True时可以创建大于 2G 的 zip 文件，默认值 True；

'''
zip_file = zipfile.ZipFile("Annotations.rar")
zip_list = zip_file.namelist() # 得到压缩包里所有文件

for f in zip_list:
    zip_file.extract(f, folder_abs) # 循环解压文件到指定目录

zip_file.close() # 关闭文件，必须有，释放内存


# rar解压


import rarfile

path = "E:\\New\\New.rar"
path2 = "E:\\New"

rf = rarfile.RarFile("Annotations.rar")
rf.extractall("./")