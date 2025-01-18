def main():
    # Initialize an empty list to store the data
    data = []

    print("Enter data (name integer1 integer2), one per line. Type 'end' to stop:")

    # Loop to read lines from standard input
    while True:
        line = input()
        if line.lower() == 'end':  # Stop reading input if 'end' is entered
            break

        # Split the line into components: name, integer1, integer2
        parts = line.split( )
        if (len(parts) != 3):
            print("Please enter a name followed by two integers.")
            continue

        name = parts[0]
        try:
            num1 = int(parts[1])
            num2 = int(parts[2])
            if num2 == 0:
                print("Cannot divide by zero. Please enter valid integers.")
                continue
            # Append a tuple (name, num1, num2, num1/num2) to the data list
            data.append((name,num1,num2, num1 / num2))  
        except ValueError:
            print("Please enter valid integers.") 
    

    # Print the header for the table
    print(f"{'Name':<10} {'Integer1':<10} {'Integer2':<10} {'Division':<10}") 

    # Print each entry in the data list
    for entry in data:
        name, num1, num2, result = entry   
        print(f"{name:<10} {num1:<10} {num2:<10} {result:<.3f}") 


if __name__ == "__main__" :
    main()