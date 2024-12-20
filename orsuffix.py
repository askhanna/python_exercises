# Function: ordinalSuffix to return the ordinal suffix of a number
def ordinalSuffix(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Determine the last digit of the number
    last_digit = int(num_str[-1])
    
    # Determine the last two digits of the number
    last_two_digits = int(num_str[-2:]) if len(num_str) > 1 else last_digit
    
    # Determine the suffix based on the last digit and last two digits
    if 10 <= last_two_digits <= 20:
        suffix = 'th'
    else:
        if last_digit == 1:
            suffix = 'st'
        elif last_digit == 2:
            suffix = 'nd'
        elif last_digit == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
    
    # Return the number with its ordinal suffix
    return num_str + suffix

# Example usage
print(ordinalSuffix(42))  # Output: 42nd
print(ordinalSuffix(1))   # Output: 1st
print(ordinalSuffix(23))  # Output: 23rd
print(ordinalSuffix(11))  # Output: 11th
print(ordinalSuffix(101)) # Output: 101st
assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'