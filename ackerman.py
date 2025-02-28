import sys

def ackerman(m,n):
    if(m == 0):
        return n + 1
    elif (m > 0 and n == 0):
        return ackerman(m - 1, 1)
    else:
        return ackerman(m - 1, ackerman(m ,n - 1))
    
if __name__ == "__main__":
    m = 3
    n = 4
    print(sys.getrecursionlimit())
    print(f"Ackerman ({m},{n}) is: {ackerman(m,n)} ") 