
def word_to_decimal(word):
    b = ord(max(word.lower()))-86
    lst = [ord(ch)-87 for ch in word.lower()]
    return sum(num*b**n for n, num in enumerate(lst[::-1]))

