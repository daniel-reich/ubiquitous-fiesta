
def next_number(n):
    s = str(n)
    for i in range(1, len(s)):
        if i + 1 <= len(s) and s[-i] > s[-i - 1]:
            for j in range(1, 9):
                x = s[-i:].find(str(int(s[-i - 1]) + j))
                if x != -1:
                    z = [s[-i - 1]] + [s[-i:-i + x]] + [s[-i + x + 1:]]
                    if -i + x + 1 >= 0:
                        z = [s[-i - 1]] + [s[-i:-i + x]]
                    add = "".join(sorted("".join(z)))
                    s = s[: -i - 1] + s[-i + x] + add
                    return int(s)
                    break
​
    return n

