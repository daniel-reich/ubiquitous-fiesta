
def repeat_string(txt, n):
    if isinstance(txt, str):
        lst = [txt] * n
        result = ''.join(lst)
    else:
        result = 'Not A String !!'
    return result

