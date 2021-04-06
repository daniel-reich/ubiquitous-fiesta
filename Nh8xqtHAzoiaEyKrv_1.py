
def correct_sentences(s):
    format = []
    xsplit =  s.split(' ')
    for i in xsplit:
        if i != '':
            format.append(i)
    for i in range(len(format)):
        if format[i] == format[i].capitalize():
            format[i-1] = format[i-1]+'.'
    format[-1] = format[-1]+'.'
    format[0] = format[0].capitalize() 
    return ' '.join(format)

