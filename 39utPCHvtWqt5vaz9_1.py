
def direction(lst):
    d = {'e': 'w', 'E': 'W', 'a': 'e', 'A': 'E'}
    return [''.join(d.get(i, i) for i in word) for word in lst]

