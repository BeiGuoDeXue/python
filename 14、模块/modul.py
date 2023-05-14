#!/usr/bin/python3
# 文件名: using_sys.py
# 模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。 

import sys
import support
 
print('命令行参数如下:')
for i in sys.argv:
   print(i)
 
print('\n\nPython 路径为：', sys.path, '\n')
# 1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
# 2、sys.argv 是一个包含命令行参数的列表。
# 3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。

# 想使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下：
# import module1[, module2[,... moduleN]

support.print_func("Runoob")


# from … import 语句
# from modname import name1[, name2[, ... nameN]]

# from … import * 语句
# 把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
# from modname import *



# __name__属性
# 一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')

# dir() 函数
# 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
print(dir(sys))
print("\n")
print(dir())


# 一种导入子模块的方法是:
# from sound.effects import echo
# 这同样会导入子模块: echo，并且他不需要那些冗长的前缀，所以他可以这样使用:
# echo.echofilter(input, output, delay=0.7, atten=4)

# 还有一种变化就是直接导入一个函数或者变量:
# from sound.effects.echo import echofilter

# 从一个包中导入*
# 导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。
# 以下实例在 file:sounds/effects/__init__.py 中包含如下代码:

# __all__ = ["echo", "surround", "reverse"]
# 这表示当你使用from sound.effects import *这种用法时，你只会导入包里面这三个子模块。
