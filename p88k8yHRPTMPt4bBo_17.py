
def count_vowels(word):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in word:
        if i in vowels:
            count += 1
    return count

