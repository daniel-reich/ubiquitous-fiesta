
def switcheroo(txt):
    txt = list(txt)
    for i in range(len(txt) - 3):
        if not txt[i+3].isalnum():
            if txt[i:i+3] == ['n', 't', 's']:
                txt[i:i+3] = ['n', 'c', 'e']
            elif txt[i:i+3] == ['n', 'c', 'e']:
                txt[i:i+3] = ['n', 't', 's']
    return "".join(txt)

