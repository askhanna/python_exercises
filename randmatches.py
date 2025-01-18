import random
import bisect
import numpy as np

def binary_search(arr,x):
    """Perform binary search to check if x is in arr."""
    idx = bisect.bisect_left(arr,x)
    if(idx != len(arr) and arr[idx] == x):
        return True
    else:
        return False
    
def count_common_element(arr1,arr2):
    """Count the number of common elements between two arrays using binary search."""
    arr1.sort()
    common_count = 0
    for i in arr2:
        if(binary_search(arr1,i)):
            common_count += 1
    
    return common_count

def experiment(N,T):
    """Run T trials of the experiment for arrays of size N."""
    total_common = 0

    for _ in range(T):
        arr1 = [random.randint(100000, 999999) for _ in range(N)]
        arr2 = [random.randint(100000, 999999) for _ in range(N)]
        
        # Count the number of common elements
        common_count = count_common_element(arr1,arr2)
        total_common += common_count

    # Return the average number of common elements
    return (total_common / T)

def main(T):
    """Run the experiment for N = 10^3, 10^4, 10^5, 10^6 and print the results."""
    Ns = [10**3, 10**4, 10**5, 10**6]

    print(f"{'N':<10} {'Average Common Elements':<25}")
    print("-" * 35)

    for N in Ns:
        avg_common = experiment(N, T)
        print(f"{N:<10} {avg_common:<25.2f}")

if __name__ == "__main__":
    # Example: Run the experiment with T trials as 10
    T = int(input("Enter the number of trials (T): "))
    main(T)




        