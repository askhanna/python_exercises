''' Write a static method histogram() that takes an array a[] of int values and
an integer M as arguments and returns an array of length M whose ith entry is the number
of times the integer i appeared in the argument array. If the values in a[] are all
between 0 and M–1, the sum of the values in the returned array should be equal to
a.length.'''

class Histogram:
    @staticmethod
    def histogram(a, M):
        # Initialize a list of length M with all elements as 0
        result = [0] * M
        
        # Iterate through each element in the input array 'a'
        for num in a:
            if 0 <= num < M:  # Check if the number is within the valid range
                result[num] += 1
                
        return result

# Example usage:
a = [1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 6]
M = 8
print(Histogram.histogram(a, M))  # Output: [0, 1, 2, 1, 3, 1]
