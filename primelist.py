def sieveofEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while p**2 <= n:
        if prime[p]:
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, n) if prime[p]] 

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def main():
    #print(sieveofEratosthenes(10001))
    n = 1
    count = 1
    while count <= 10001:
        n += 1
        if isPrime(n):
            #print(n)
            count += 1
        
    print(f"{n} is the 10001st prime number.") 

if __name__ == "__main__":
    main()