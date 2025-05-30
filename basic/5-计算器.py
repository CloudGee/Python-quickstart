print("This is a calculator program.")
print(
"""
1, add
3, subtract
2, multiply
4, divide
""")

choice = input("Please choose an operation (1-4): ")
num1 = float(input("Please input the first number: "))
num2 = float(input("Please input the second number: "))
if choice == '1':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")
elif choice == '2':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")
elif choice == '3':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")
elif choice == '4':
    result = num1 / num2
    print(f"The result of {num1} / {num2} is: {result}")
else:
    print("Invalid choice. Please choose a valid operation (1-4).")