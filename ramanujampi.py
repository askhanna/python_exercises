import math

def ramanujan_pi(n):
  """
  Approximates 1/pi using Ramanujan's infinite series.

  Args:
    n: The number of terms to calculate.

  Returns:
    The approximate value of 1/pi.
  """

  pi_sum = 0
  k = 0
  factorial = 1

  for _ in range(n):
    pi_sum +=  (math.factorial(4*k) * (1103 + 26390 * k))/(math.factorial(k)**4 * 396**(4*k))
    k = k + 1
    #factorial = factorial * -1
  return ((pi_sum) * (2 * 2**0.5 / 9801))
 

if __name__ == "__main__":
  print("Calculating 1/pi..")
  n = input("Enter number of iterations to calculate pi: ")
  print(f"pi = {1/ramanujan_pi(int(n))}")