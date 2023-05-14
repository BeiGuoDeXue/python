#/usr/bin/python3

# Python 中的循环语句有 for 和 while。

while False:
    print(False)
else:
    print(True)

# Python for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串。

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    print(site)


# 也可用于打印字符串中的每个字符：
word = 'runoob'
 
for letter in word:
    print(letter)

# 在 Python 中，for...else 语句用于在循环结束后执行一段代码。
for x in range(6):
  print(x)
else:
  print("Finally finished!")


# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
# continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
# Python pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句