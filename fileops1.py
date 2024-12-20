def writeToFile(filename, text):
    # Open the file in write mode:
    with open(filename, 'w') as fileObj:
        # Write the text to the file:
        fileObj.write(text)

def appendToFile(filename, text):
    # Open the file in append mode:
    with open(filename, 'a') as fileObj:
        # Write the text to the end of the file:
        fileObj.write(text)

def readFromFile(filename):
    # Open the file in read mode:
    with open(filename) as fileObj:
        # Read all of the text in the file and return it as a string:
        return fileObj.read()
    
def readLinesFromFile(filename):
    # Open the file in read mode:
    with open(filename) as fileObj:
        # Read all of the lines in the file and return them as a list:
        return fileObj.readlines()
    
def readLineFromFile(filename, lineNumber):
    # Open the file in read mode:
    with open(filename) as fileObj:
        # Read all of the lines in the file and return the line at the specified line number:
        return fileObj.readlines()[lineNumber]

def writeToFileWithNewline(filename, text):
    # Open the file in write mode:
    with open(filename,'w') as fileObj:
            # Write the text to the file:
            fileObj.write(text + '\n')

def appendToFileWithNewline(filename, text):
    # Open the file in append mode:
    with open(filename, 'a') as fileObj:
        # Write the text to the end of the file:
        fileObj.write(text + '\n')

def readLinesFromFileWithNewline(filename):
    # Open the file in read mode:
    with open(filename) as fileObj:
        # Read all of the lines in the file and return them as a list:
        return fileObj.readlines()
    
def readLineFromFileWithNewline(filename, lineNumber):
    # Open the file in read mode:
    with open(filename) as fileObj:
        # Read all of the lines in the file and return the line at the specified line number:
        return fileObj.readlines()[lineNumber]
    
def writeToFileWithNewline(filename, text):
    # Open the file in write mode:
    with open(filename, 'w') as fileObj:
        # Write the text to the file:
        fileObj.write(text + '\n')

def appendToFileWithNewline(filename, text):
    # Open the file in append mode:
    with open(filename, 'a') as fileObj:
        # Write the text to the end of the file:
        fileObj.write(text + '\n')

writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
print(readFromFile('greet.txt'))



