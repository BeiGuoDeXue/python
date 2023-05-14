#usr/bin/python3.8

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# file: 必需，文件路径（相对或者绝对路径）。
# mode: 可选，文件打开模式
# buffering: 设置缓冲
# encoding: 一般使用utf8
# errors: 报错级别
# newline: 区分换行符
# closefd: 传入的file参数类型
# opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。

# 打开一个文件
f = open("/tmp/foo.txt", mode = 'w')

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
f.close()

f = open("/tmp/foo.txt", mode = 'r')
str = f.read()
print(str)

# 关闭打开的文件
f.close()
