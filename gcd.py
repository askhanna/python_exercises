def gcdfunc(a,b):
    if (b == 0):
        return a
    else:
        rem = a % b
        return gcdfunc (b,rem)

if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if (a < b):
        x = gcdfunc (b,a)
    else:
        x = gcdfunc(a,b)
    print(f"GCD of {a} and {b} is {x}")
