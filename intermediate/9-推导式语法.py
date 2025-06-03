n = range(10)
# for i in n:
#   print(i)
a = { i**2 for i in n if i % 2 == 0 }
print(type(a))