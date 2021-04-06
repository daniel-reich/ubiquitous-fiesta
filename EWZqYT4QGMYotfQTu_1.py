
ABC = 'abcdefghijlmnopqrstuvwxyz'
​
def tap_code(text):
    def dots(ch):
        n = 2 if ch == 'k' else ABC.index(ch)
        return '.'*(n//5) + '. .' + '.'*(n%5)
    
    if ' ' in text:
        s = [len(dots)-1 for dots in text.split()]
        return ''.join(ABC[i*5+j] for i, j in zip(s[::2], s[1::2]))
    return ' '.join(dots(ch) for ch in text)

