set1 = set()
set2 = set([1,1,2,3])
set3 = {1, 2, 3, 3}
print(set3)
print(set3.pop())
set4 = {"a", "c", "d"}
print(set4)
print(set4.pop())

# Set Methods:
## add("element"): Add an element to the set.
## remove("element"): Remove the specified element from the set.
## discard("element"): Remove the specified element from the set if present.
## pop(): Remove a random element from the set.
## clear(): Remove all elements from the set.

# Method Definitions:
fruits = {"apple", "banana", "orange", "mango", "cherry", "grape", "pear"}

# add("element"): Add an element to the set.
fruits.add("watermelon")
# 添加 'watermelon' 后的集合: {'grape', 'apple', 'banana', 'pear', 'cherry', 'mango', 'orange', 'watermelon'}
print("添加 'watermelon' 后的集合:", fruits)

# remove("element"): Remove the specified element from the set.
fruits.remove("orange") # 元素"orange"若不在集合中会报错
# 删除 'orange' 后的集合: {'grape', 'apple', 'banana', 'pear', 'cherry', 'mango', 'watermelon'}
print("删除 'orange' 后的集合:", fruits)

# discard("element"): Remove the specified element from the set if present.
fruits.discard("papaya")  # 元素 'papaya' 不在集合中，不会报错
# 删除 'papaya' 后的集合: {'grape', 'apple', 'banana', 'pear', 'cherry', 'mango', 'watermelon'}
print("删除 'papaya' 后的集合:", fruits)

# pop(): Remove a random element from the set.
removed_element = fruits.pop()
# 随机删除的元素: grape
# 集合变为的内容: {'apple', 'banana', 'pear', 'cherry', 'mango', 'watermelon'}
print("随机删除的元素:", removed_element)
print("集合变为的内容:", fruits)

# clear(): Remove all elements from the set.
fruits.clear()
# 清空集合后的内容: set()
print("清空集合后的内容:", fruits)


# Set Operations:
## - : Difference (差集)
## & : Intersection (交集)
## | : Union (并集、合集)
## != : Not equal to (不等于)
## == : Equal to (等于)

# Set Definitions:
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}
set_C = {1, 1, 3, 2, 5, 4}

# - : Difference (差集)
difference_set = set_A - set_B
# 集合A与集合B的差集: {1, 2, 3}
print("集合A与集合B的差集:", difference_set)

# & : Intersection (交集)
intersection_set = set_A & set_B
# 集合A与集合B的交集: {4, 5}
print("集合A与集合B的交集:", intersection_set)

# | : Union (并集、合集)
union_set = set_A | set_B
# 集合A与集合B的并集: {1, 2, 3, 4, 5, 6, 7, 8}
print("集合A与集合B的并集:", union_set)

# != : Not equal to (不等于)
is_not_equal = set_A != set_B
# 集合A与集合B是否不相等: True
print("集合A与集合B是否不相等:", is_not_equal)
# 集合A与集合C是否不相等: False
print("集合A与集合C是否不相等:", set_A != set_C)

# == : Equal to (等于)
is_equal = set_A == set_B
# 集合A与集合B是否相等: False
print("集合A与集合B是否相等:", is_equal)
# 集合A与集合C是否相等: True
print("集合A与集合C是否相等:", set_A == set_C)