
def increment_string(txt):  
  t,d = ''.join(i for i in txt if i.isalpha()), ''.join(i for i in txt if i.isdigit())
  return txt+'1' if not d else t + str(int(d) + 1).rjust(len(d),'0')

