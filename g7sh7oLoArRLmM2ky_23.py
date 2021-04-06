
import string
def baconify(msg, mask=None):
    a = {'a': 'uuuuu','b': 'uuuul','c': 'uuulu','d': 'uuull','e': 'uuluu','f': 'uulul','g': 'uullu','h': 'uulll','i': 'uluuu','j': 'uluul','k': 'ululu','l': 'ulull','m': 'ulluu','n': 'ullul','o': 'ulllu','p': 'ullll','q': 'luuuu','r': 'luuul','s': 'luulu','t': 'luull','u': 'luluu','v': 'lulul','w': 'lullu','x': 'lulll','y': 'lluuu','z': 'lluul','.': 'llllu',' ': 'lllll'}
    b = {'uuuuu': 'a', 'uuuul': 'b', 'uuulu': 'c', 'uuull': 'd', 'uuluu': 'e', 'uulul': 'f', 'uullu': 'g', 'uulll': 'h', 'uluuu': 'i', 'uluul': 'j', 'ululu': 'k', 'ulull': 'l', 'ulluu': 'm', 'ullul': 'n', 'ulllu': 'o', 'ullll': 'p', 'luuuu': 'q', 'luuul': 'r', 'luulu': 's', 'luull': 't', 'luluu': 'u', 'lulul': 'v', 'lullu': 'w', 'lulll': 'x', 'lluuu': 'y', 'lluul': 'z', 'llllu': '.', 'lllll': ' '}
    if not mask:
        msg = msg.replace(' ', '').translate(str.maketrans('', '', string.punctuation))
        cipher = [msg[x:x+5]for x in range(0, 5 * (len(msg) // 5), 5)]
        code = [''.join(['l' if y.islower() else 'u' for y in x])for x in cipher]
        return ''.join([b[x] for x in code])
    else:
        msg = msg.lower().translate(str.maketrans(' ', ' ', string.punctuation.replace('.', '')))
        code = ''.join([a[x] for x in msg])
        y = ' '.join([a[x] for x in msg])
        cipher =  ''
        
        i = 0
        for x in mask:
            if i == len(code):
                cipher += x
                continue
​
            if x == ' ' or x in string.punctuation:
                cipher += x
                continue
            elif code[i] == 'u':
                cipher += x.upper()
            elif code[i] == 'l':
                cipher += x.lower()
                
            i += 1
        return cipher

