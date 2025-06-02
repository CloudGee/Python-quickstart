sum_func = lambda *args:sum(args)
print(sum_func(1,2,3))

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)  # 输出：['Bob', 'Eva', 'Alice', 'David', 'Charlie']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出：[2, 4, 6, 8]