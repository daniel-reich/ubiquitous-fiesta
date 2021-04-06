
def join(lst):
    output = lst.pop(0)
    n = 0
    for word in lst:
        for i in range(1, len(output) + 1):
            substring = output[-i:]
            if word.startswith(substring):
                output += word[i:]
                if n == 0 or i < n:
                    n = i
                break
        else:
            output += word
    return [output, n]

