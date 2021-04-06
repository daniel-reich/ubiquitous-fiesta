
def common_last_vowel(txt):
    ll = []
    for i in txt:
        if i[-1] in "aeiouAEIOU":
            ll.append(i.lower())
    return (ll)[-1]

