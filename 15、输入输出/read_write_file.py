#usr/bin/python3.8

# 读和写文件
# open() 将会返回一个 file 对象，基本语法格式如下:

# open(filename, mode)
# filename：包含了你要访问的文件名称的字符串值。
# mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。

# 打开一个文件
f = open("/tmp/foo.txt", "w")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
f.close()

f = open("/tmp/foo.txt", "r")
str = f.read()
print(str)

# 关闭打开的文件
f.close()
