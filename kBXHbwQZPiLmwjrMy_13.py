
def translate_word(s):
    vows = 'aoueiAOUEI'
    if not s:
        return s
    if s[0] in vows:
        return s + "yay"
    for i in range(1, len(s)):
        if s[i] in vows:
            if s[0].isupper():
                return s[i].upper() + s[i+1:] + s[0].lower() + s[1:i] + 'ay'
            else:
                return s[i:] + s[:i] + 'ay'
​
​
def translate_sentence(s):
    ws = []
    for w in s.split():
        i, j = 0, len(w)-1
        while i < len(w) and not w[i].isalpha():
            i += 1
        while j > i and not w[j].isalpha():
            j -= 1
        w_strip = w[i:j+1]
        ws.append(w[:i] + translate_word(w_strip) + w[j+1:])
    return ' '.join(ws)

