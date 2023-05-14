#!/usr/bin/python3

'''
+ 字符串连接                a+b
* 输出重复字符串             a*2   
[] 索引
[:] 截取
in 成员运算符，包含返回True
not in
r/R 原始字符串
% 格式字符串
'''

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if ("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')


# 格式化输出，使用%隔开“”，不是，

print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

# python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。实例如下
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)


# f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去，实例如下：
name = 'Runoob'
str = f'Hello {name}'  # 替换变量
print(str)

w = {'name': 'Runoob', 'url': 'www.runoob.com'}
str = f'{w["name"]}: {w["url"]}'
print(str)

# Unicode 字符串
# 在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集。使用的语法是在字符串前面加上前缀 u。
# 在Python3中，所有的字符串都是Unicode字符串。


