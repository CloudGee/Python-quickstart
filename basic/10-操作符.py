a = 1
b = 1
print(id(a))
print(id(b))
print(a is b)  # Output: True
# 在Python中，整数、字符串、以及其他一些不可变对象都有一个小整数缓存池（interning pool），用于存储频繁使用的小整数和短字符串，以节省内存和提高性能。
# 当你创建一个整数对象时，如果它的值在缓存池中存在，Python会重用已存在的对象而不是创建一个新的对象。这意味着对于小整数，Python会尽量避免重复创建，而是引用已存在的对象。

x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(id(x))
print(id(y))
print(id(z))

result_is = x is y
print("Result of 'x is y':", result_is)
# Output: Result of 'x is y': True

result_is_not = x is not z
print("Result of 'x is not z':", result_is_not)
# Output: Result of 'x is not z': True