
from copy import deepcopy
​
def count_word(table, word):
    cnt = 0
    ans = deepcopy(table)
    H, W = len(table), len(table[0])
    for i in range(H):
        table[i] = ''.join(table[i])
    ttable = [''.join(list(i)) for i in zip(*table)]
    L = len(word)
    # find horizontal words:
    for r in range(H):
        row = table[r]
        for idx in range(W - L + 1):
            if word in [row[idx:idx+L], row[idx:idx+L][::-1]]:
                cnt += 1
                for c in range(idx, idx + L):
                    ans[r][c] = ans[r][c].lower()
    # find vertical words:
    for r in range(W):
        row = ttable[r]
        for idx in range(H - L + 1):
            if word in [row[idx:idx+L], row[idx:idx+L][::-1]]:
                cnt += 1
                for c in range(idx, idx + L):
                    ans[c][r] = ans[c][r].lower()
    # find diagonal words, upper left to lower right:
    for row in range(H):
        for col in range(W):
            for dr, dc in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
                r, c = row, col
                diag = ""
                while 0 <= r < H and 0 <= c < W and len(diag) < L:
                    diag += table[r][c]
                    r += dr
                    c += dc
                if word == diag:
                    cnt += 1
                    r, c = row, col
                    for i in range(L):
                        ans[r][c] = ans[r][c].lower()
                        r += dr
                        c += dc
    return (cnt, ans)

