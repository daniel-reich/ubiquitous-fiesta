
def validate_email(txt):
    a = txt.split('@')
    if a[0] == txt or a[0] == '':
      return False
    name = a[0]
    try:
      domain = str(a[1]).split('.')[0]
      tld = str(a[1]).split('.')[1]
    except:
      return False
    return True

