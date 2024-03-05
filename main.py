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
        temp = ""
        for j in range(i, length):
            if L[j]:
                if temp in words:
                    L[i] = True
                    break
            temp += w[j]
        else:
            if temp in words:
                L[i] = True
    if L[0]:
        return True
    else:
        for i in range(len(L)):
            if L[i]:
                print(f"The nearest true index is at {i}")
                for j in range(i, i+10):
                    print(w[j], end="")
                print("\n")
                break
        return False


def min_penalty(h, loc):
    N = len(h)
    P = [float('inf')]*N
    P[0] = 0
    path = [0] * N

    # Calculate minimum penalty for reaching each hotel
    for i in range(1, N):
        for j in range(i):
            penalty = (200 - (loc[i] - loc[j]))**2
            if P[i] > P[j] + penalty:
                P[i] = P[j] + penalty
                path[i] = j
    print(P)
    # Find the path and total penalty
    final_path = [N-1]
    current = N-1
    total_penalty = P[N-1]

    while current > 0:
        current = path[current]
        final_path.insert(0, current)

    return total_penalty, final_path


if __name__ == "__main__":
    print("Starting main.")
    h = ['Hotel1', 'Hotel2', 'Hotel3', 'Hotel4', 'Hotel5', 'Hotel6', 'Hotel7', 'Hotel8', 'Hotel9', 'Hotel10', 'Hotel11',
         'Hotel12', 'Hotel13', 'Hotel14', 'Hotel15']
    loc = [0, 175, 215, 280, 400, 450, 560, 640, 780, 820, 1000, 1060, 1140, 1190, 1260, 1350]
    total_penalty, final_path = min_penalty(h, loc)
    print("Total penalty:", total_penalty)
    print("Hotels path:", [h[i] for i in final_path])
    print("Done.")
