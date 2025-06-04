import argparse

# create the parser
parser = argparse.ArgumentParser(description="A simple calculator")

# add the arguments
parser.add_argument("num1", type=int, help="First num to add")
parser.add_argument("num2", type=int, help="Second num to add")

# parse the arguments
args = parser.parse_args()

try:
    print(args.num1 + args.num2)
except AttributeError:
    print("Please enter two numbers")