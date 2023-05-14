#/usr/bin/python3

# Python 条件语句是通过一条或多条语句的执行结果（True 或者 False）来决定执行的代码块。
# 1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
# 2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
# 3、在 Python 中没有 switch...case 语句，但在 Python3.10 版本添加了 match...case，功能也类似，详见下文。

a = 3

if a == 1:
    print("a", a)
elif a == 2:
    print("a", a)
else :
    print("a", a)

# python 3.10 support
# match a:
#     case 1 :
#         print("a", a)
#     case 2 :
#         print("a", a)
#     case 3 :
#         print("a", a)
