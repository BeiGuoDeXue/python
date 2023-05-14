#usr/bin/python3.8

# 输出： print、表达式语句
# 第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
# 如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
# 如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。



# str.format() 的基本使用如下:
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
# 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
# 在括号中的数字用于指向传入对象在 format() 中的位置，如下所示：

print('{1} 和 {0}'.format('Google', 'Runoob'))

# 可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
import math
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

# 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))


# 旧式字符串格式化
# % 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串. 例如:
print('常量 PI 的值近似为：%5.3f。' % math.pi)










