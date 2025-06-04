import sys

print(sys.argv) # print system arguments in list

print("Script name:", sys.argv[0])

# print first argument
if len(sys.argv) > 1:
    print("First argument:", sys.argv[1])

def add(a: float, b: float) -> float:
    return a + b

if len(sys.argv) != 3:
    print("Usage: python3 9-commandline2.py <a> <b>")
    sys.exit(1)
else:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        print(f"{a} + {b} = {add(a, b)}")
    except ValueError:
        print("Invalid input, must be a number")
        sys.exit(1)