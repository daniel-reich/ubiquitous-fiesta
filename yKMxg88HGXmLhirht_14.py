
def add_letters(lst):
    r = [ord(i) - 96 for i in lst]
    if not lst:
      return 'z'    
    elif sum(r) > 26:
      return chr(sum(r) % 26 + 96)
    else:
      return chr(sum(r) + 96)

