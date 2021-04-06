
def validate_email(txt):
  return True if "@" in txt and "." in txt and len(txt[:txt.index("@")]) > 1 and "." in txt[txt.index("@")+1:] else False

