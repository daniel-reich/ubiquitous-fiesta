
punct = {' ', '.', ',', '?', "'", ":", ";", "!"}
alpha = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
​
​
def vigenere(text='', keyword=''):
    size = len(alpha)
    letters_dict = {}
    inverse_dict = {}
    for i in range(size):
        letters_dict[alpha[i]] = i
        inverse_dict[i] = alpha[i]
​
    v_table = [['']*size for x in range(size)]
    for r in range(size):
        for c in range(size):
            v_table[r][c] = inverse_dict[(c+r) % size]
​
    cipher = True
    if ' ' not in text:
        cipher = False
​
    for delim in punct:
        text = text.replace(delim, "")
    plain_text = text.upper()
    keyword = keyword.upper()
    cipher_text = ""
    l_t, l_k = len(text), len(keyword)
    new_text = ""
    for i in range(l_t):
        cipher_text += keyword[i % l_k]
        row = letters_dict[cipher_text[i]]
        if cipher:
            col = letters_dict[plain_text[i]]
            new_text += v_table[row][col]
        else:
            col = (letters_dict[plain_text[i]] - row) % size
            new_text += v_table[0][col]
    return new_text

