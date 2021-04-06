
def is_palindrome_possible(txt):
    if txt == txt[::-1]:
        return True
    elif sorted(txt) == sorted(set(txt)):
        return False
​
    single = []
    for c in set(txt):
        if txt.count(c) == 1:
            single.append(c)
    if len(single) > 1:
        return False
    
    palindrome = [single[0]] if single else []
    letters = [ch for ch in txt if txt.count(ch) >= 2]
​
    i = 0
    while len(palindrome) < len(txt):
        curr_count, curr_ch = letters.count(letters[i]), letters[i]
        for j in range(curr_count - 1):
            palindrome.append(curr_ch)
            palindrome.insert(0, curr_ch)
        for k in range(curr_count):
            letters.remove(curr_ch)
​
    return palindrome == palindrome[::-1]

