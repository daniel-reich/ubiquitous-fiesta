
def keyboard_shortcut(txt):
  current = ''
  clip = ''
  
  for s in txt.split('Ctrl + '):
    if s[0] == 'C':
      clip = current
    if s[0] == 'V':
      current += clip
    current += s.lstrip('CV ')
    
  return current.strip()

