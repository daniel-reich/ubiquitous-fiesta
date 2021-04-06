
# Fix this incorrect code, so that all tests pass!
def remove_vowels(string):
    import re
    pattern = re.compile(r'[b-dB-Df-hF-Hk-nK-Np-zP-Z]+')
    matches = pattern.findall(string)
    return "".join(matches)

