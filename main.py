def longest_increasing_subsequence(V):
    n = len(V)
    L = [1]*n

    # Compute optimized L[] values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if V[i] > V[j] and L[i] < L[j] + 1:
                L[i] = L[j]+1

    # Initialize maximum to 0 to get the maximum of all L[i]
    maximum = 0
    idx = 0

    # Pick maximum of all L values
    for i in range(len(L)):
        if maximum < L[i]:
            maximum = L[i]
            idx = i

    seq = [V[idx]]
    while idx != 0:
        for i in range(idx-1, -1, -1):
            if L[i] == L[idx]-1 and V[i] < V[idx]:
                seq.insert(0, V[i])
                idx = i
                break

    return seq


if __name__ == "__main__":
    print("Starting main.")
    ex = [36, 13, 78, 85, 16, 52, 58, 61, 63, 83, 46, 19, 85, 1, 58, 71, 26, 26, 21, 31]
    result = longest_increasing_subsequence(ex)
    print(result)
    print("Done.")
