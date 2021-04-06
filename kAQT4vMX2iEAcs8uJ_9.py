
def longest_7segment_word(lst):
    longest = ''
    for word in lst:
        have_it = False
        for letter in word:
            if letter in 'k, m, v, w, x':
                have_it = True
                break
        if have_it:
            continue
        else:
            if len(word) > len(longest):
                longest = word
​
    return longest

