import random

def getSmallest(numbers):
    # If the numbers list is empty, return None:
    if not numbers:
        return None
    # Otherwise, return the smallest number in the list:

    # Create a variable that tracks the smallest value so far, and start
    # it off a the first value in the list:
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num  # Update the smallest value so far
    return smallest