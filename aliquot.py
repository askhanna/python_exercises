import matplotlib.pyplot as plt

def sum_of_proper_divisors(n):
    if n <= 1:
        return 0
    divisor_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                divisor_sum += n // i
    return divisor_sum

def aliquot_sequence(start, max_terms=20):
    sequence = [start]
    for _ in range(max_terms - 1):
        next_term = sum_of_proper_divisors(sequence[-1])
        if next_term == 0 or next_term in sequence:
            break
        sequence.append(next_term)
    return sequence

def print_sequence(sequence):
    print(" -> ".join(map(str, sequence)))

def plot_sequence(sequence):
    plt.figure(figsize=(12, 6))
    plt.plot(range(len(sequence)), sequence, marker='o')
    plt.title(f"Aliquot Sequence starting from {sequence[0]}")
    plt.xlabel("Term Number")
    plt.ylabel("Value")
    plt.grid(True)
    
    # Annotate each point with its value
    for i, val in enumerate(sequence):
        plt.annotate(str(val), (i, val), textcoords="offset points", xytext=(0,10), ha='center')

    # Highlight the start and end points
    plt.plot(0, sequence[0], 'go', markersize=10, label='Start')
    plt.plot(len(sequence)-1, sequence[-1], 'ro', markersize=10, label='End')
    
    plt.legend()
    plt.show()

# Get input from the user
start = int(input("Enter the starting number for the aliquot sequence: "))
max_terms = int(input("Enter the maximum number of terms to generate: "))

# Generate the sequence
sequence = aliquot_sequence(start, max_terms)

print(f"\nAliquot sequence starting from {start}:")
print_sequence(sequence)

# Analyze the sequence
if len(sequence) == max_terms:
    print(f"\nReached the maximum number of terms ({max_terms}).")
elif sequence[-1] == 0:
    print("\nThe sequence terminated at 0 (reached a prime number).")
elif sequence[-1] in sequence[:-1]:
    cycle_start = sequence.index(sequence[-1])
    print(f"\nFound a cycle of length {len(sequence) - cycle_start}.")
    print("Cycle:", end=" ")
    print_sequence(sequence[cycle_start:])
else:
    print("\nThe sequence terminated.")

# Plot the sequence
plot_sequence(sequence)