
def bifid(text):
    letters = 'abcdefghiklmnopqrstuvwxyzj'
    codes = ['11', '12', '13', '14', '15', '21', '22', '23', '24', '25',
             '31', '32', '33', '34', '35', '41', '42', '43', '44', '45',
             '51', '52', '53', '54', '55', '24']
    if ' ' in text:
        codes_lst = [codes[letters.index(c.lower())]
                     for c in text if c.isalpha()]
        upper_deck, lower_deck = zip(*codes_lst)
        pairs = ''.join(upper_deck)
        pairs += ''.join(lower_deck)
        return ''.join(letters[codes.index(pairs[i * 2: i * 2 + 2])]
                       for i in range(len(pairs) // 2))
    else:
        codes_str = ''.join(codes[letters.index(c)] for c in text)
        upper_deck = codes_str[:len(codes_str) // 2]
        lower_deck = codes_str[len(codes_str) // 2:]
        codes_lst = [upper_deck[i] + lower_deck[i]
                     for i in range(len(upper_deck))]
        return ''.join(letters[codes.index(c)] for c in codes_lst)

