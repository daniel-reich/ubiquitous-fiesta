
def validate_email(txt):
  return txt.count('@') == 1 and txt[0] !='@' and txt.count('.')>= 1 and \
  txt[txt.index('@') + 1:].count('.') >= 1

