
def secret(text):
  tag, *rest = text.split('.')
  return "<{0} class='{1}'></{0}>".format(tag, ' '.join(rest))

