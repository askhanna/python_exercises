def drawBox(width, height):
    print('+', '-' * (width - 2), '+', sep='')
    for i in range(height - 2):
        print('|', ' ' * (width - 2), '|', sep='')  
    print('+', '-' * (width - 2), '+', sep='')

def main():
    width = int(input("Enter the width of the box: "))
    height = int(input("Enter the height of the box: "))
    drawBox(width, height)
    return

if __name__ == "__main__":
    main()