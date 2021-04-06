
def wurst_is_better(txt):
    sausages = ['kielbasa', 'chorizo', 'moronga', 'salami', 'sausage', 'andouille',
                'naem', 'merguez', 'gurka', 'snorkers', 'pepperoni']
    for x in sausages:
        txt = txt.replace(x, 'Wurst')
        txt = txt.replace(x.capitalize(), 'Wurst')
    return txt

