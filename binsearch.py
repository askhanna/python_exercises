def binsearch(lst,low, high, val):
    if high >= low:
        mid = low + (high - low) // 2

        if lst[mid] == val:
            return mid
        elif val < lst[mid]:
            return binsearch(lst,low,mid - 1,val)
        elif(val > lst[mid]):
            return binsearch(lst,mid + 1,high,val)
    else:
        return -1;


if __name__ == "__main__":
    lst = [3,9,27,98,102,220,228,506,786,1000]
    val = input("Enter number to search: ")
    idx = binsearch(lst,0,len(lst) - 1,int(val))
    if idx != -1:
        print(f"The number {val} is found at position {idx}")
    else:
        print(f"The number {val} was not found in the list.")
    
