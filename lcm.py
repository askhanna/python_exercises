def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a,b):
    return a * b // gcd(a,b)

def main():
    a, b = map(int, input().split())
    print(f"GCD: {gcd(a, b)}")
    print(f"LCM: {lcm(a, b)}")

if __name__ == '__main__':
    #main()
    lcm = 2520
    for i in range(11,21):
        lcm = lcm * i // gcd(lcm, i)
    print(f"LCM of numbers upto 20 is {lcm}")