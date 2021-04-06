
def to_camel_case(txt):
  if '-' in txt:
    lst = txt.split('-')
    return ''.join([lst[i].title() if i!=0 else lst[i] for i in range(len(lst))])
  elif '_' in txt:
    lst = txt.split('_')
    return ''.join([lst[i].title() if i!=0 else lst[i] for i in range(len(lst))])
  else:
    return ''

