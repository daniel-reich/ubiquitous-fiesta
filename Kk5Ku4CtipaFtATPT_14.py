
def coconut_translator(txt):
    ans = list(map(lambda x:bin(ord(x))[2:].rjust(8,'0'),list(txt)))
    def c(x):
        t = list('coconuts')
        ans = ''.join(list(map(lambda y: t.pop(0).upper() if y == '1' else t.pop(0), x)))
        t = list('coconuts')
        return ans
    return ' '.join(list(map(lambda x:c(x),ans)))

