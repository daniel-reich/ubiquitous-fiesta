
def hidden_anagram(text, phrase):
    txt = [c.lower() for c in text if c.isalpha()]
    phr = [c.lower() for c in phrase if c.isalpha()]
    len_txt, len_phr = len(txt), len(phr)
    for start in range(len_txt - len_phr + 1):
        if txt[start] in phr:
            tmp_phr = phr.copy()
            for i in range(len_phr):
                if txt[start + i] in tmp_phr:
                    j = tmp_phr.index(txt[start + i])
                    tmp_phr = tmp_phr[:j] + tmp_phr[j + 1:]
                else:
                    break
            if not tmp_phr:
                return ''.join(c for c in txt[start: start + len_phr])
    return 'noutfond'

