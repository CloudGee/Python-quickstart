# my_list = [1,2,3]
# my_iter = iter(my_list)
# print(my_iter)
# for i in my_iter:
#   print(i)

def squares(n):
    for i in range(1, n + 1):
        yield i * i

for square in squares(5):
    print(square)