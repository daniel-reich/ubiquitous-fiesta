
def validate_relationships(txt):
  txt = txt.replace('=','==').replace('<==','<=').replace('>==','>=')
  return eval(txt)

