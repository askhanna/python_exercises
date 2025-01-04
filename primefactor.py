import math

def primefactor(num):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num = num / 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num = num / i
    if num > 2:
        factors.append(num)
    return factors

def main():
    print(primefactor(600851475143))
    print(primefactor(45))
    print(primefactor(100))
    print(primefactor(36))


if __name__ == "__main__":
    main()