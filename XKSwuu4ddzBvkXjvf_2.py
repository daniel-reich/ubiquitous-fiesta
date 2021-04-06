
sieve = [1] * 10000
def prime_calc():
    global sieve
    for i in range(2, int(9999**0.5)+1):
        if sieve[i] == 1:
            for j in range(2, 9999):
                if i*j > 9999:
                    break
                sieve[i*j] = 0
def sentence_primeness(sentence):
    prime_calc()
    l1 = [chr(Z) for Z in range(ord('a'),ord('z')+1)]
    lp = [Z-ord('a')+1 for Z in range(ord('a'),ord('z')+1)]
    for Z in range(ord('0'), ord('9') + 1):
        l1.append(chr(Z))
        lp.append(int(chr(Z)))
    l1.append(' ')
    lp.append(0)
    st = ''.join([Z for Z in sentence if Z.lower() in l1])
    l2 = st.split()
    lw = [sum(lp[l1.index(Z)] for Z in st.lower()) for st in l2]
    tot = sum(lw)
    if sieve[tot] == 1:
        return "Prime Sentence"
    for i in range(0, len(l2)) :
        if sieve[tot-lw[i]] == 1:
            return "Almost Prime Sentence (" + l2[i] + ")"
    from itertools import combinations
    for i in range(len(l2)-1, 0, -1):
        lo = list(combinations(lw, i))
        if any(True for Z in lo if sieve[sum(Z)] == 1): return "Composite Sentence"
    # it wrong but ....
    return "Composite Sentence"

