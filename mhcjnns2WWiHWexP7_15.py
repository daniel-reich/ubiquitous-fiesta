
def calculate_arrowhead(lst):
    x= ''.join(i for i in lst)
    l=[x.count('>')-x.count('<') for i in x if x.count('>')-x.count('<')>0 ]
    k=[x.count('<')-x.count('>') for i in x if x.count('<')-x.count('>')>0 ]
    if x.count('>')>x.count('<'):
        return max(l)*'>'
    if x.count('<')>x.count('>'):
        return max(k)*'<'
    return ''

