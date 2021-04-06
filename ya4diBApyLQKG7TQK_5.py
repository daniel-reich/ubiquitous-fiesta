
def validate_relationships(txt):
  txt = txt.replace('=','==')
  txt = txt.replace('<==','<=').replace('>==','>=')
  return eval(txt)

