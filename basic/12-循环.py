# fruits = ["apple", "banana", "orange"]
# computer = {"CPU": {"I7": {"Level 1": "64K", "Level 2": "8192K"}}, "BIOS": "ASUS"}

# # i, j, k, v
# for f in fruits:
#     print(f)
# # apple
# # banana
# # orange

# for k, v in enumerate(fruits):
#     print(f"The {k} value in list is {v}")
# # The 0 value in list is apple
# # The 1 value in list is banana
# # The 2 value in list is orange

# for i in range(3):
#     print(i)
# # 0
# # 1
# # 2

# for j in range(5, 10, 2):
#     print(j)
# # 5
# # 7
# # 9

# for key, value in computer.items():
#     print(f"{key} is {value}.")
# for key in computer.keys():
#     print(f"{key} is {computer[key]}.")
# # CPU is {'I7': {'Level 1': '64K', 'Level 2': '8192K'}}.
# # BIOS is ASUS.

# for item in computer.items():
#     print(f"{item}") # Will print as a tuple
# # ('CPU', {'I7': {'Level 1': '64K', 'Level 2': '8192K'}})
# # ('BIOS', 'ASUS')

# for i in range(1, 10):
#   for j in range(i, 10):
#     print(f"{i} * {j} = {i*j}", end=" ")
#   print()

# print("=============")
# for i in range(9, 0, -1):
#   for j in range(i, 10):
#     pass

# if a > 1:
#   pass

# num = 0
# while num < 5:
#     print(num)
#     num += 1

# # 使用 break 终止循环
# num = 0
# while True:
#     print(num)
#     num += 1
#     if num >= 5:
#         break
# # 0
# # 1
# # 2
# # 3
# # 4

# # 使用 continue 跳过当前迭代
# num = 0
# while num < 5:
#     num += 1
#     if num == 3:
#         continue
#     print(num)
# 1
# 2
# 4
# 5

count = 0
while True:
    if count < 3:
        name = input("Please enter your username: ").strip()  # .strip() to remove leading and trailing whitespaces
        if len(name) == 0:
            print("Input cannot be empty!")
            count += 1
            continue
        elif name == "Haoyun":
            print("Login successful.")
            break
        else:
            print("Invalid username, please try again!")
    else:
        print("Exceeded maximum error attempts, exiting!")
        break
    count += 1