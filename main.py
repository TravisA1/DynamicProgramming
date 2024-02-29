import typing
from typing import List, Set


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
        else:
            break

    return seq


def min_coins(C, N):
    # Initialize num_coins array
    num_coins = [0] + [float('inf')]*N
    coins_used = [0] + [-1]*N

    # Compute minimum coins required for all values from 1 to N
    for n in range(1, N+1):
        for c in C:
            if n-c >= 0 and num_coins[n-c] + 1 < num_coins[n]:
                num_coins[n] = num_coins[n-c] + 1
                coins_used[n] = c

    # Construct the list of coins used
    if num_coins[N] == float('inf'):
        return None
    else:
        coins = []
        while N > 0:
            coins.append(coins_used[N])
            N -= coins_used[N]
        return coins


def load_words_from_file() -> Set[str]:
    result = set()
    with open('word_list_moby_crossword_flat.txt', 'r') as ins:
        for line in ins:
            temp = line.split('\n')
            result.add(temp[0])
    return result


def word_string_checker(w: str) -> bool:
    words = load_words_from_file()
    length = len(w)
    L = [False] * length
    for i in range(length-1, -1, -1):
        temp = w[i]
        for j in range(i, length):
            if L[j]:
                if temp in words:
                    L[i] = True
                    break
            temp += w[j]
    if L[0]:
        return True
    else:
        return False


if __name__ == "__main__":
    print("Starting main.")
    # ex = [2, 22, 32, 35, 66, 59, 79, 64, 48, 96, 7, 39, 18, 15, 45, 89, 3, 81, 26, 26, 31,
    #       55, 10, 91, 70, 61, 12, 87, 13, 31, 27, 58, 71, 75, 32, 63, 98, 77, 92, 43, 66, 32,
    #       11, 65, 1, 80, 14, 99, 29, 91]
    # result = longest_increasing_subsequence(ex)
    # print(result)
    # C = [1, 4, 9, 15, 25, 40, 75, 100]
    # for i in range(1, 201):
    #     print(f"{i}  {min_coins(C, i)}")
    thing = input("Give the string thing that you wanna test: ")
    print(word_string_checker(thing))
    print("Done.")
