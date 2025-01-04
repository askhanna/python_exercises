import math

def ispalindrome(n):
    return str(n) == str(n)[::-1] 

def largestfactor(num):
    for i in range(int(math.sqrt(num)), 1, -1): 
        if num % i == 0 and len(str(i)) == 3 and len(str(num//i)) == 3:  # Check if the number is divisible by i and i is a 3-digit number
            return [i, num // i] 
    return [num]  # If no factors found, return the number itself


def main():
    for num in range(1000000,0,-1):
        if ispalindrome(num):
            
            factors = largestfactor(num)
            if len(factors) == 2:
                print(f"Largest factors of the palindrome number {num} are: {factors[0]} and {factors[1]}")
                break

if __name__ == "__main__":
    main()
