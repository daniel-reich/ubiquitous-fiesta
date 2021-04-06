
def digital_vowel_ban(n, ban):
    d = {'e': '0135789', 'i': '5689', 'o': '0124', 'u': '4'}
    new = ''.join(i for i in str(n) if i not in d.get(ban, ''))
    return 'Banned Number' if not new else int(new)

