
def emotify(txt):
  return txt.replace('smile',':D') if 'smile' in txt else txt.replace('grin',':)') if 'grin' in txt else txt.replace('sad',':(') if 'sad' in txt else txt.replace('mad',':P')

