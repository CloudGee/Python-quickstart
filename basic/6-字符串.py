# 字符串加法，字符串拼接
str1 = 'hello' + " world"
print(str1)  # 输出: hello world

# 列表
list1 = ['hello', 'world', "!"]
print(list1)  # 输出: ['hello', 'world', '!']

print(" ! ".join(list1))

str2 = "hello world \n !"
print(len(str2))  # 输出: 15

string = "hello world."
print(len(string))
print(string[0])
print(string[-1])

# 左闭右开区间
print(string[0:3])
print(string[0:len(string)+1])
print(string[0:13:2])