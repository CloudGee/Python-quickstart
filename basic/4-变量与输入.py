name = "aaa"
age = 18
nameAge = "aaa 18"
NameAge = "aaa 18"
name_age = "aaa 18"
print(name, age, nameAge, NameAge, name_age)

name, age = "bbb", 20
print(name, age)  # 输出 bbb 20

print("name:", name, "\n", "age:", age)  # 输出 name: bbb

# 格式化输出f-string
print(f"name: {name} \n age: {age}")  # 输出 name: bbb, age: 20
print("\\n")

# %s -> 字符串, %d -> 整数, %f -> 浮点数
print("name: %s \n age: %d" % (name, age))  # 输出 name: bbb, age: 20
print("name: %s" % "aaa")  # 输出 name: aaa

floadN=1.111111
print("floadN: %.2f" % floadN)  # 输出 floadN: 1.11，保留两位小数

a = 1
a += 1
print(a)  # 输出 2

print("\\\\")
print("\"")

print(
    "Line 1\nLine 2\n\"Line 3\"\n\tLine 4\nLine \
5\n'Line 6'\n\\"
)

name = input("Please input your name: ")
print(name)