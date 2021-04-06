
def club_entry(word):
    chars =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    word_list = list(word)
​
    i = 0
​
    for char in word_list:
        i += 1
        try:
            if char == word_list[i]:
                letter = char
        except IndexError:
            pass
​
​
    chars_index = chars.index(letter)
    return (chars_index + 1) * 4
​
print(club_entry("hill"))

