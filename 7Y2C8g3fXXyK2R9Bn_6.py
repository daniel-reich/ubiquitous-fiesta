
def keyword_cipher(key, message):
    unique_key = ""
    for c in key:
        if c not in unique_key:
            unique_key += c
    alphabet = (unique_key + "".join(chr(97 + i) for i in range(26)
                if chr(97 + i) not in unique_key))
    return "".join(alphabet[ord(c) - 97] if 96 < ord(c) < 123 else c
                   for c in message)

