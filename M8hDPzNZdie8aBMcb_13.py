
def count_substring(x):
    return len(list(filter(lambda x: x[0]=='A' and x[-1]=='X',[x[i: j] for i in range(len(x)) for j in range(i + 1, len(x) + 1)])))

