
def validate_email(string):
  return True if ((string.find("@")>1) and (string.rfind(".")>string.find("@"))) else False

