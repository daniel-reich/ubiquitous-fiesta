
def find_longest(s):
    n_letters = []
    longest_word = ''
​
    for i in s.split():
        n_letters.append(len(i))
​
        for j in s.split():
            if len(j) == max(n_letters):
                longest_word = j
​
        if "." in longest_word:
            longest_word = longest_word[:-1]
​
        elif "!" in longest_word:
            longest_word = longest_word[:-1]
​
        elif "'s" in longest_word:
            longest_word = longest_word[:-2]
​
        if '\"' in longest_word:
            longest_word = longest_word[1:-1]
​
    return longest_word.lower()

