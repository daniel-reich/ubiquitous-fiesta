
def emotify(txt):
    d = {'smile':':D',
         'grin':':)',
         'sad':':(',
         'mad':':P'}
    for k, v in d.items():
        txt = txt.replace(k, v)
    return txt

