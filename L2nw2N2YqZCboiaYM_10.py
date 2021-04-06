
def repeated(s):
    word, len_w, len_s = "", 0, len(s)
    for i in range(len_s//2):
        word, len_w, ok  = word + s[i], len_w + 1, True
        for j in range(len_w, len_s, len_w):
            if word != s[j:j+len_w]: ok = False; break
        if ok: return True
    return False

