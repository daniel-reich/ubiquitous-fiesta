
def fib_str(n, txt):
    for index in range(2, n):
        txt.append(txt[index - 1] + txt[index - 2])
    return ", ".join(txt)

