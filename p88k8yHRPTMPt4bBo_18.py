
def count_vowels(txt):
    vowels = "aeiou"
    total = 0
    for i in txt:
        for j in vowels:
            if j == i:
                total += 1
    return total

