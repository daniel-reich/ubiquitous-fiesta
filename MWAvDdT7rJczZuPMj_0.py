
def count_word(grid, word):
    w1 = list(word.lower())
    w2 = list(word[::-1].lower())
    word = list(word)
    matches = (word, word[::-1])
​
    r = len(grid[0])
    step = len(word)
​
    s = list(' '.join(''.join(i) for i in grid))
    s_copy = s[:]
    total = 0
​
    for i in range(len(s)):
        if s[i:i+step] in matches: #horizontal
            s_copy[i:i+step] = w1 if s[i] == word[0] else w2
            total += 1
        if s[i:i+(r+1)*step:r+1] in matches: #vertical
            s_copy[i:i+(r+1)*step:r+1] = w1 if s[i] == word[0] else w2
            total += 1
        if s[i:i+r*step:r] in matches: #diagonal-left
            s_copy[i:i+r*step:r] = w1 if s[i] == word[0] else w2
            total += 1
        if s[i:i+(r+2)*step:r+2] in matches: #diagonal-right
            s_copy[i:i+(r+2)*step:r+2] = w1 if s[i] == word[0] else w2
            total += 1
​
    res = [list(i) for i in ''.join(s_copy).split(' ')]
    return total, res

