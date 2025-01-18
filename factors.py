import matplotlib.pyplot as plt

''' display factors of a number > 2'''
def getfactors(n):
    factors = []
    for i in range(1, n//2 + 1):
        if n%i == 0:
            factors.append(i)

    return factors

'''n = 24
factors = getfactors(n)
print(f"Factors of {n} are {factors}")
print(f"Sum of factors of {n} are {sum(factors)}")
'''
def aliquotseq(start,max_terms = 20):
        num = start
        factors = []
        result = [start]
        factsum = 0
        for i in range(max_terms):
             factors = getfactors(num)
             factsum  = sum(factors)
             result.append(factsum)
             if(factsum == 1):
                break
             num = factsum
        return result

def print_seq(sequence):
     print(" -> ".join(map(str, sequence)))

def plot_sequence(seq):
     plt.figure(figsize=(12,6))
     plt.plot(range(len(seq)),seq, marker = 'o')
     plt.title(f"Aliquot sequence starting from {seq[0]}")
     plt.xlabel("Term Number")
     plt.ylabel("Value")
     plt.grid(True)
     plt.legend()
     plt.show()


start = int(input("Enter the starting number for the aliquot sequence: "))
max_terms = int(input("Enter the maximum number of terms to generate: "))
seq = aliquotseq(start,max_terms)
print_seq(seq)
plot_sequence(seq)

