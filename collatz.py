def sequence(n):
    i = 0
    while n != 1:
        i= i+1
        print(f"Iteration {i}, n: {n}")
        if n % 2 == 0: # n is even
            n = n / 2
        else: # n is odd
            n = n*3 + 1
    print(f"We reqched 1 in {i} iterations")

if __name__ == "__main__":
    i = int(input("Enter a +ve number: "))
    print(f"Calling Collatz Sequence function..")
    sequence(i)
            