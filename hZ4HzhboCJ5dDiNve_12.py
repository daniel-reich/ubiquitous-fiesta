
def special_reverse_string(txt):
    l = [i.casefold() for i in txt if i != ' '][::-1]
    for i, val in enumerate(txt):
        if val == ' ':
            l.insert(i, val)
    return ''.join(
      k.swapcase() if not i.islower() and i.isalpha() 
      else k
      for i, k in zip(txt, l))

