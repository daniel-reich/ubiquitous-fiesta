
def correct_signs(txt):
  x = [i for i in txt if i in '<>']
  t = txt.replace(' <', '').replace(' >', '').split()
  return all(int(t[i])<int(t[i+1]) if x[i]=='<' else int(t[i])>int(t[i+1]) for i in range(len(t)-1))

