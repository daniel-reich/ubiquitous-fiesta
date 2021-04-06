
def encrypt(word):
    def code(l):
        vowels = {'a': '0', 'e': "1", "o": "2", "u": "3"}
        if l in vowels:
            return vowels[l]
        else:
            return l
    return ''.join( list(map(code,list(word[::-1]))) ) + 'aca'

