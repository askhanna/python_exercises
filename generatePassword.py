import random
import string

# Create string constants that for each type of character:
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '1234567890'
SPECIAL = '~!@#$%^&*()_+'

def generatePassword(length):
    if length < 12:
        length = 12

    ALL_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL
    password1 = ''.join(random.choices(ALL_CHARS,k=length))
    
    password2 = []
    password2.append(random.choice(LOWER_LETTERS))
    password2.append(random.choice(UPPER_LETTERS))
    password2.append(random.choice(NUMBERS))
    password2.append(random.choice(SPECIAL))
    password2[4:length - 1] = random.choices(ALL_CHARS,k=length-4)
    random.shuffle(password2)
    password2 = ''.join(password2)
    return password1, password2

if __name__ == "__main__":
    pwd1, pwd2 = generatePassword(12)
    print(f"Password1: {pwd1}")
    print(f"Password2: {pwd2}")
    


