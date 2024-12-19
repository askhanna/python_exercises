def fizzbuzz(upTo):
    # Loop from 1 up to (and including) the upTo parameter:
    for num in range(1, upTo + 1):
        if (num % 3 == 0) and (num % 5 == 0):
            print("FizzBuzz", end=' ') 
        elif (num % 3 == 0):
            print("Fizz", end=' ')
        elif (num % 5 == 0):
            print("Buzz", end=' ')
        else:
            print(num, end=' ')

if __name__ == "__main__":
    upTo = input("Enter Upto number: ")
    fizzbuzz(upTo)