
def word_search(s, words):
    v = ''.join(''.join(s[i] for i in range(64) if i%8==j) for j in range(8))
    chunks8 = [s[i:i+8] for i in range(0,64,8)]
    dr = [' '*i+chunks8[i]+' '*(7-i) for i in range(8)]
    dl = [' '*(7-i)+chunks8[i]+' '*i for i in range(8)]
    dr1 = ''.join(''.join(i[j] for i in dr) for j in range(15))
    dl1 = ''.join(''.join(i[j] for i in dl) for j in range(15))
    altogether = (s+s[::-1]+v+v[::-1]+dr1+dr1[::-1]+dl1+dl1[::-1]).lower()
    return all(i in altogether for i in words)

