
def same_vowel_group(w):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = set()
    words = dict()
    ordered_list = []
    for vowel in vowels:
        for char in w[0]:
            if vowel == char:
                vowel_list.add(vowel)
    for word in w:
        vowel_comparison = set()
        for char in word:
            for vowel in vowels:
                if vowel == char:
                    vowel_comparison.add(vowel)
        if vowel_list == vowel_comparison:
            words[word] = ''
    for word in w:
        if word in list(words):
            ordered_list.append(word)
    return ordered_list

