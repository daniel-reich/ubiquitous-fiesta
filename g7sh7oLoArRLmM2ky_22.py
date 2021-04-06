
letter_to_code = {
    "a": "uuuuu",
    "b": "uuuul",
    "c": "uuulu",
    "d": "uuull",
    "e": "uuluu",
    "f": "uulul",
    "g": "uullu",
    "h": "uulll",
    "i": "uluuu",
    "j": "uluul",
    "k": "ululu",
    "l": "ulull",
    "m": "ulluu",
    "n": "ullul",
    "o": "ulllu",
    "p": "ullll",
    "q": "luuuu",
    "r": "luuul",
    "s": "luulu",
    "t": "luull",
    "u": "luluu",
    "v": "lulul",
    "w": "lullu",
    "x": "lulll",
    "y": "lluuu",
    "z": "lluul",
    ".": "llllu",
    " ": "lllll"
}
code_to_letter = {
    "uuuuu": "a",
    "uuuul": "b",
    "uuulu": "c",
    "uuull": "d",
    "uuluu": "e",
    "uulul": "f",
    "uullu": "g",
    "uulll": "h",
    "uluuu": "i",
    "uluul": "j",
    "ululu": "k",
    "ulull": "l",
    "ulluu": "m",
    "ullul": "n",
    "ulllu": "o",
    "ullll": "p",
    "luuuu": "q",
    "luuul": "r",
    "luulu": "s",
    "luull": "t",
    "luluu": "u",
    "lulul": "v",
    "lullu": "w",
    "lulll": "x",
    "lluuu": "y",
    "lluul": "z",
    "llllu": ".",
    "lllll": " "
}
​
​
def baconify(msg, mask=None):
    if not mask:
        cipher_text = ''.join(c for c in msg if c.isalpha())
        deciphered = ''
        while len(cipher_text) >= 5:
            chunk = cipher_text[:5]
            cipher_text = cipher_text[5:]
            code = ''.join('u' if c.isupper() else 'l' for c in chunk)
            deciphered += code_to_letter[code]
        return deciphered
    else:
        mask_idx = 0
        encipher = ''
        for letter in msg:
            if letter.isalpha() or letter in '. ':
                code = letter_to_code[letter.lower()]
                code_idx = 0
                while code_idx < 5:
                    if mask[mask_idx].isalpha():
                        if code[code_idx] == 'u':
                            encipher += mask[mask_idx].upper()
                        elif code[code_idx] == 'l':
                            encipher += mask[mask_idx].lower()
                        code_idx += 1
                    else:
                        encipher += mask[mask_idx]
                    mask_idx += 1
        encipher += mask[mask_idx:]
        return encipher

