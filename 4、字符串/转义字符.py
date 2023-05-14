#!/usr/bin/python3

# 转义字符

# 实测无用
print("\a")
# 退格，只退一个空格
print("Hello \b  World!")
# 空，和\0 \00感觉一样
print("\000")
# 纵向制表符（纵向换行，缩进一格）
print("a\vb\vc")
# 横向制表符（从开头空余8个空格）
print("a\tbb")
# \r,回车，将 \r 后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r 后面的内容完全替换完成。
print('google runoob taobao\r123456')
# \f, 换页（没看出来效果）
print("Hello \f World!")
# \yyy,八进制数，y 代表 0~7 的字符，例如：\012 代表换行。
print("\110\145\154\154\157\40\127\157\162\154\144\41")
# \xyy,十六进制数
print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")






