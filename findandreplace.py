# Write a findAndReplace() function that has three parameters: 
# text is the string with text to be replaced, 
# oldText is the text to be replaced, and newText is the replacement text. Keep in mind that this function must be case-sensitive: if you are replacing 'dog' with 'fox', then the 'DOG' in 'MY DOG JONESY' won’t be replaced.

def findAndReplace(text, oldText, newText):
    return text.replace(oldText, newText)

if __name__ == "__main__":
    print(findAndReplace("I like dogs", "dogs", "cats"))
    print(findAndReplace("I like dogs", "dog", "cat"))
    print(findAndReplace("I like dogs", "DOG", "cat"))
    print(findAndReplace("I like dogs", "DOG", "CAT"))