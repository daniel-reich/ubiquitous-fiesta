
def digital_vowel_ban(n, ban):
    d = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four',
         '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
    ans = ''
    s = str(n)
    for x in s:
        if ban not in d[x]:
            ans = ans + x
    if not ans:
        return "Banned Number"
    return int(ans)

