
def blah_blah(txt, n):
    txt = txt.split()
    return ' '.join(txt[0:-n]) + ' blah' * n  + '...' if n < len(txt) else 'blah ' * (len(txt) - 1) + 'blah...'

