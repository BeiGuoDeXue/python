#/usr/bin/python3

# Python 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体。

# [表达式 for 变量 in 列表] 
# [out_exp_res for out_exp in input_list]
# 或者 
# [表达式 for 变量 in 列表 if 条件]
# [out_exp_res for out_exp in input_list if condition]
# 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper()for name in names if len(name)>3]
print(new_names)

# 计算 30 以内可以被 3 整除的整数：
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)


# 字典推导式
# { key_expr: value_expr for value in collection }
# 或
# { key_expr: value_expr for value in collection if condition }

# 使用字符串及其长度创建字典：

listdemo = ['Google','Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key:len(key) for key in listdemo}
print(newdict)

dic = {i:i**2 for i in (1,2,3)}
print(dic)

# 集合推导式
# 集合推导式基本格式：
# { expression for item in Sequence }
# 或
# { expression for item in Sequence if conditional }

# 计算数字 1,2,3 的平方数：
setnew = {i**2 for i in (1,2,3)}
print(setnew)

# 判断不是 abc 的字母并输出：
print("-----------------集合-----------------------")
setne = {x for x in 'adshkkhfas' if x not in 'abc'}
print(setne)
print(type(setne))

print("-----------------元组-----------------------")
# 元组推导式（生成器表达式）
# 元组推导式可以利用 range 区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组。
# 元组推导式基本格式：
# (expression for item in Sequence )
# 或
# (expression for item in Sequence if conditional )
# 元组推导式和列表推导式的用法也完全相同，只是元组推导式是用 () 圆括号将各部分括起来
# 另外元组推导式返回的结果是一个生成器对象
a = (x for x in range(1,10))
print(a)        # 返回的是生成器对象
tuple(a)        # 使用 tuple() 函数，可以直接将生成器对象转换成元组，这里失败了
print(a)
