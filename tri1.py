a = input("Enter num1: ")
b = input("Enter num2: ")
c = input("Enter num3: ")

print(f"You have entered {a}, {b} and {c}")

if (int(a) + int(b) > int (c)):
    if (int(c) + int(b) > int (a)):
        if (int(c) + int(a) > int (b)):
            print("It is a valid triangle")
        else:
            print("It is not a valid triangle")
    else:
            print("It is not a valid triangle")
else:
            print("It is not a valid triangle")