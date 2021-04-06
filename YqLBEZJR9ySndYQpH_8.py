
def staircase(n):
    total = []
    for i in range(1, int(str(n).lstrip('-'))+1):
        string = ''
        string = string + ('_' * (int(str(n).lstrip('-'))-i)) + ('#' * i)
        total.append(string)
    if '-' in str(n):
        print(total)
        total.reverse()
​
    return '\n'.join(total)

