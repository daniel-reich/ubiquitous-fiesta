
def dial(txt):
    phone_lookup = {'abc': 2, 'def': 3, 'ghi': 4,
                    'jkl': 5, 'mno': 6, 'pqrs': 7,
                    'tuv': 8, 'wxyz': 9}
​
    for k in phone_lookup:
        for c in k:
            if c in txt.lower():
                txt = txt.lower().replace(c, str(phone_lookup[k]))
​
    return txt

