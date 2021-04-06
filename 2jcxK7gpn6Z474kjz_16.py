
def security(txt):
    txt_x = ''
    for letter in txt:
        if letter != 'x':
            txt_x += letter
    for i in range(1, len(txt_x) - 1):
​
        if txt_x[i] == '$':
            if txt_x[i + 1] == 'T' or txt_x[i - 1] == 'T':
                return "ALARM!"
    return "Safe"

