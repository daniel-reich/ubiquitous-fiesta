
def monkey_talk(txt):
  sol = ['eek' if i[0].lower() in 'aeiou' else 'ook' for i in txt.split()]
  sol[0]= sol[0].title()
  
  return ' '.join(sol) + '.'

