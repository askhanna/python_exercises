def abs(x):
    if x < 0:
        return -x
    else:
        return x

def round(x):
    return int(x + 0.5)

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def sqrt(x):
    return x**0.5

def hypotenuse(a, b):
    return sqrt(a**2 + b**2)

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def toBinary(x):
    return bin(x)[2:]


if __name__ == "__main__":
    print(f"abs(-10) = {abs(-10)}")
    print(f"round(10.5) = {round(10.5)}")
    print(f"isPrime(10) = {isPrime(10)}")
    print(f"sqrt(16) = {sqrt(16)}")
    print(f"hypotenuse(3, 4) = {hypotenuse(3, 4)}") 
    print(f"toBinary(50) = {toBinary(50)}")
    print(f"binary_search([1, 2, 3, 4, 5], 8) = {binary_search([1, 2, 3, 4, 5], 8)}")
    print(f"transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) = {transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])}")
    print(f"factorial(5) = {factorial(5)}")

