
import re
​
def c_cipher(msg, keyword):
    #print(f'msg={msg}, keyword={keyword}')
    order = []
    for i, c in enumerate(keyword):
        order.append((c, i))
    order.sort(key=lambda e: e[0])
    #print(f'order={order}')
    out = ''
    msg2 = re.sub(r'[,.!?; ]', '', msg.lower())
    msg2 = msg2 + (((len(keyword) - len(msg2) % len(keyword)) * 'x') \
                     if len(msg2) % len(keyword) != 0 else '')
    cryptic = []
    for seg in range(len(msg2) // len(keyword)):
        cryptic.append(msg2[seg*len(keyword):(seg+1)*len(keyword)])
    #print(f'cryptic={cryptic}')
    if msg.find(' ') != -1: #encrypt
        for o in order:
            for s in cryptic:
                out += s[o[1]]
    else:   #decrypt
        out = ['?' for c in msg]
        for c, o in enumerate(order):
            for r in range(len(msg) // len(keyword)):
                out[r*len(keyword)+o[1]] = msg[c*len(msg)//len(keyword)+r]
                #print(f'out={out}')
        out = ''.join(out)
​
    return out

