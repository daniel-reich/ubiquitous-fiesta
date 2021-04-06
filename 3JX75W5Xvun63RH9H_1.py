
def describe_num(n):
    words = ('exciting', 'fantastic', 'virtuous', 
             'heart-warming', 'tear-jerking', 'beautiful', 
             'exhillarating', 'emotional', 'inspiring')
​
    group = ' '.join(i for val, i in enumerate(words, 2) if not n%val)
    return 'The most brilliant {} number is {}!'.format(group, n).replace('  ', ' ')

