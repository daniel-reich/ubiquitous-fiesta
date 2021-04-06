
def count_same_ends(txt):
    words = ''.join(i for i in txt if i == ' ' or i.isalpha()).lower().split(' ')
    return sum(1 for word in words if len(word) != 1 and word[0] == word[-1])

