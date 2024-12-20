import random

def mode(numlst):
    if len(numlst) == 0:
        return None
    modeDict = {}
    maxFreqNum = None
    maxFreq = 0

    for num in numlst:
        if num not in modeDict:
            modeDict[num] = 1
        else:
            modeDict[num] += 1
        
        if modeDict[num] > maxFreq:
            maxFreqNum = num
            maxFreq = modeDict[num]

    return maxFreqNum, maxFreq

if __name__ == "__main__":
    random.seed(42)
    testData = [1, 2, 3, 4, 4, 7, 8, 8, 8, 8, 9, 10, 10, 10, 10]
    for i in range(1000):
        random.shuffle(testData)
    mod, count = mode(testData)
    print(f"Mode is {mod} and number of occurence is {count}")  # Output: 1
