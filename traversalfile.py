'''
本文件总结一些常用到的几种文件所在路径的处理方式
'''
import os
import sys

'''1.获取和改变文件所在的路径的一些函数'''


os.getcwd()
os.path.abspath('.')


#获取当前文件所在文件夹的父文件夹路径
os.path.abspath('..')

#改变当前目录
#os.chdir("E:\\")#更改完毕后，打开文件的目录会在foldPath之后了。
os.getcwd()


#组合路径返回


    

#def getCurrentPath():
#    return os.

#获取当前文件所在文件夹路径
print(os.getcwd())
print(os.path.abspath('.'))
print(os.path.abspath(os.curdir))

#获取当前文件所在文件夹的父文件夹路径
print(os.path.abspath('..'))

#改变当前目录
os.chdir('W:/20181115/ProcessImage/')
print(os.getcwd())
#之后如果做 test1 = open('file1.txt')则会是‘E:\files\file1.txt’

#组合路径,如果有相同前缀，则合并前缀，否则就添在末尾,
#支持两个以上多个路径合并
print(os.path.join('W:','W:\\20181115','20180105\\ProcessImage'))
name = "text.txt"
print(os.path.join(os.getcwd(),name))

print(os.walk(os.getcwd()))

#可以打印路径下所有文件,对于每个文件夹，都有三个，文件夹路径，文件夹里的文件夹名，文件夹里的文件名
def file_name(filePath):
    root  
    for root, dirs, files in os.walk(filePath):
        print("_____________")
        print(root)
        print(dirs)
        print(files)
        print("")
file_name(os.path.join(os.getcwd(),'m_042','TextureReplace'))

