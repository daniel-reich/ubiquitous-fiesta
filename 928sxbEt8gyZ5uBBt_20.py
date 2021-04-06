
def wurst_is_better(txt):
    lst_wurst = ['kielbasa', 'chorizo', 'moronga', 'salami', 'sausage',
                 'andouille', 'naem', 'merguez', 'gurka', 'snorkers',
                 'pepperoni']
    lst = txt.split()
    for i, w in enumerate(lst):
        if w.lower() in lst_wurst:
            lst[i] = 'Wurst'
    return ' '.join(lst)

