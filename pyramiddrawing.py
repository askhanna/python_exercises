def drawPyramid(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))
    return

def main():
    height = int(input("Enter the height of the pyramid: "))
    drawPyramid(height)
    return

if __name__ == "__main__":
    main()