
def validate_spelling(txt):
    strList = txt.split('. ')
    word = ''.join([i for i in strList.pop(-1) if i.isalpha()]).lower()
    return ''.join(strList).lower() == word

