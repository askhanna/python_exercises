def get_stats(ids):
    """
    Given a list of integers, return a dictionary of counts of consecutive pairs
    Example: [1, 2, 3, 1, 2] -> {(1, 2): 2, (2, 3): 1, (3, 1): 1}
    """
    counts = {}
    for pair in zip(ids, ids[1:]):
        counts[pair] = counts.get(pair,0) + 1
    return counts

if __name__ == "__main__":
    lst = [1, 2, 3, 1, 2]
    pair_st = get_stats(lst)
    result = ' '.join(str(key) + ": " + str(value) + " , " for key, value in pair_st.items())
    print(result)