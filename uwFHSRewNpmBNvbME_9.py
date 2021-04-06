
def same_vowel_group(w):
    main_vowels = {v for v in w[0] if v in ('a', 'e', 'i', 'o', 'u')}
    group = []
    for word in w:
        vowels = {v for v in word if v in ('a', 'e', 'i', 'o', 'u')}
        if main_vowels == vowels:
            group.append(word)
    return group

