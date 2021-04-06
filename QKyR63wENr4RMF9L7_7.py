
def tweak_letters(txt, lst):
  return ''.join(['a' if txt[i]=='z' and lst[i]==1 else 'z' if txt[i]=='a' and lst[i]==-1 else chr(ord(txt[i])+lst[i]) for i in range(len(txt))])

