
def paul_cipher(txt):
    shift = 0
    ans = ""
    for c in txt.upper():
        if c.isalpha():
            ans += chr(65 + ((ord(c) - 65) + shift) % 26)
            shift = ord(c) - 64
        else:
            ans += c
    return ans

