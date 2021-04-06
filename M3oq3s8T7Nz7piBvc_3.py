
def even_odd_string(txt):
    even,odd='',''
    for i,j in enumerate(txt):
        if i%2==0:
          even+=j
        if i%2!=0:
            odd+=j
    return '{} {}'.format(even,odd)

