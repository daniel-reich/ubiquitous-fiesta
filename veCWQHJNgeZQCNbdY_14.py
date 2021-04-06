
def root_digit(n):
    if len(str(n))<2:
        return n
    return root_digit(sum(map(int,str(n))))

