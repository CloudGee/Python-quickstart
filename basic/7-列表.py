# index(value): Get the index of the specified element in the list.
fruits = ["apple", "banana", "orange", "banana", "grape"]
intList = [3, 3, 1, 6, 7]


### 查
index = fruits.index("orange")
# 元素 'orange' 的索引位置: 2
print("元素 'orange' 的索引位置: %d" % index)

# count(value): Count the occurrences of the specified element in the list.
count_banana = fruits.count("banana")
# 元素 'banana' 出现的次数: 2
print("元素 'banana' 出现的次数: %d" % count_banana)

# reverse(): Reverse the order of elements in the list.
intList.reverse()
# 倒序排序后的列表: [7, 6, 1, 3, 3]
print("倒序排序后的列表: %s" % intList)

# sort(): Sort the elements in ascending order.
intList.sort()
# 汉字则按照ascil码进行排序
# 排序后的列表: 1, 3, 3, 6, 7
print("排序后的列表: %s" % intList)


## 增
# append(value): Append an element to the end of the list.
fruits.append("pear")
# 追加 'pear' 后的列表: ['apple', 'banana', 'banana', 'grape', 'orange', 'pear']
print("追加 'pear' 后的列表: %s" % fruits)

# insert(index, value): Insert an element at the specified index in the list.
fruits.insert(2, "mango")
# 在索引2处插入 'mango' 后的列表: ['apple', 'banana', 'mango', 'banana', 'grape', 'orange', 'pear']
print("在索引2处插入 'mango' 后的列表: %s" % fruits)


## 改
# computer[index] = "元素": Modify the value at the specified index in the list.
fruits[3] = "cherry"
# 将索引3处的元素改为 'cherry': ['apple', 'banana', 'mango', 'cherry', 'grape', 'orange', 'pear']
print("将索引3处的元素改为 'cherry': %s" % fruits)


## 删
# remove(value): Remove the first occurrence of the specified element from the list.
fruits.remove("apple")
# 删除 'apple' 后的列表: ['banana', 'mango', 'cherry', 'grape', 'orange', 'pear']
print("删除 'apple' 后的列表: %s" % fruits)

# pop(index=-1): Remove the element at the specified index and return it. Default value is -1.
removed_element = fruits.pop(-1)
# 删除索引1处的元素并返回索引: 'mango'，列表变为: ['banana', 'cherry', 'grape', 'orange', 'pear']
print("删除索引1处的元素并返回索引: %s，列表变为: %s" % (removed_element, fruits))



strList = list("str list hello world.")
print(strList)
print(len(strList))
print(strList[1])
print(strList[0:2])
print(strList[0:len(strList)+1:2])

# 删除列表方式1
del(fruits[0])
print(fruits)
del(fruits[0:2])
print(fruits)
del fruits[:]
print(fruits)

# 删除列表方式2
fruits = []


# 创建一个空的动态列表
dynamic_list = []

# 向列表中动态添加元素
dynamic_list.append(1)
dynamic_list.append("apple")
dynamic_list.append(True)

# index 0: <class 'int'>
# index 1: <class 'str'>
# index 2: <class 'bool'>
print(range(len(dynamic_list)))
for i in range(len(dynamic_list)):
    print(f"index {i}: {type(dynamic_list[i])}")

print(dynamic_list)  # 输出: [1, 'apple', True]

# 修改列表中的元素
dynamic_list[1] = "banana"
print(dynamic_list)  # 输出: [1, 'banana', True]


# 从列表中删除元素
dynamic_list.remove(1)
print(dynamic_list)  # 输出: ['banana', True]

# 向列表中动态添加多个元素
dynamic_list.extend([3.14, "orange"])
print(dynamic_list)  # 输出: ['banana', True,


for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
"""
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
"""

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)