
def tap_code(text):
    a = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 2, 'l': 10, 'm': 11, 'n': 12, 'o': 13, 'p': 14, 'q': 15, 'r': 16, 's': 17, 't': 18, 'u': 19, 'v': 20, 'w': 21, 'x': 22, 'y': 23, 'z': 24}
    b = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'l', 11: 'm', 12: 'n', 13: 'o', 14: 'p', 15: 'q', 16: 'r', 17: 's', 18: 't', 19: 'u', 20: 'v', 21: 'w', 22: 'x', 23: 'y', 24: 'z'}
    if '.' not in text:
        return ' '.join(['.' * (a[x]//5+1) + ' ' + '.'  * (a[x]%5+1) for x in text])
    else:
        text = text.split()
        text = [text[x:x+2] for x in range(0, len(text), 2)]
        return ''.join([b[(len(x)-1)*5+(len(y)-1)] for x, y in text])

