
def countVowels(string):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    return len([s for s in string if s in vowels])

