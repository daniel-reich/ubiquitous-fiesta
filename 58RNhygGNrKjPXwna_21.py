
def longest_nonrepeating_substring(txt):
    word, solution, repeat, maxi, start = "", "", {}, 0, 0
    for i in range(len(txt)):
        letter = txt[i]; word += letter
        if letter in repeat and repeat[letter] >= start:
            start = repeat[letter] + 1; word = txt[start:i+1]
        repeat[letter] = i
        if len(word) > maxi:
            maxi, solution = len(word), word
    return solution

