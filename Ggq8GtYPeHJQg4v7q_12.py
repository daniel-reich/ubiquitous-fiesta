
def replace_vowels(txt, ch):
        for l in txt:
                if l in 'aeiouAEIOU':
                        txt = txt.replace(l,ch)
        return txt

