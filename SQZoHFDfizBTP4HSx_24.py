
def missing_alphabets(txt):
    alphabet = [chr(i) for i in range(97,123)]
    count_max = 0
    for ch in alphabet:
        if txt.count(ch) > count_max:
            count_max = txt.count(ch)
    result = ''
    for ch in alphabet:
        result += (count_max - txt.count(ch)) * ch
    return result

