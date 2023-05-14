#/usr/bin/python3

# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：
# d = {key1 : value1, key2 : value2, key3 : value3 }

# 键必须是唯一的，不能使用列表当作键，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字。

d = {'key1':1, 'key2':2}
print(d)
print("Length:", len(d))
print ("d['key1']: ", d['key1'])
d['key1'] = 8               # 更新 key1
print ("d['key1']: ", d['key1'])
del d['key1'] # 删除键 'Name'
print ("d['key2']: ", d['key2'])
d.clear()     # 清空字典
del d         # 删除字典

# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
tinydict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print ("tinydict['Name']: ", tinydict['Name'])



x = True
country_counter = {}
print("len", len(country_counter))
def addone(country):
    if country in country_counter:
        #  错误的操作
        country_counter[country] += 1   
    else:
        country_counter[country] = 1

addone('China')
addone('Japan')
addone('china')

print(len(country_counter))
