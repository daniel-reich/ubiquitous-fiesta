
def inator_inator(inv):
  return inv + ('-' if inv[len(inv)-1].lower() in ('aeiou') else '') + 'inator ' + str(len(inv)*1000)

