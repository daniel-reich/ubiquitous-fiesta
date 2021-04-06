
def monkey_talk(txt):
  a=txt.split()
  ans=[]
  for i in a:
    if i[0] in 'aeiouAEUIO':ans.append('eek')
    else:ans.append('ook')
  return ' '.join(ans).capitalize()+'.'

