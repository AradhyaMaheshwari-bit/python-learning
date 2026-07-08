import argparse

parser = argparse.ArgumentParser(description="Simple Calculator")

parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("Operation", choices=["add", "sub", "div", "mul"], help="Operation to perform")

args = parser.parse_args()

print(args)

if(args.Operation == "add"):
    print(f"The result is {args.num1 + args.num2}")
elif(args.Operation == "sub"):
    print(f"The result is {args.num1 - args.num2}")
elif(args.Operation == "mul"):
    print(f"The result is {args.num1 * args.num2}")
elif(args.Operation == "div"):
    print(f"The result is {args.num1 / args.num2}")
else:
    print("Some error occured!!")

# if __name__ == "__main__ ":
#     main()
