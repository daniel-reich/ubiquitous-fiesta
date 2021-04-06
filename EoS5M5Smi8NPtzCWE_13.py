
def secret(text):
  tag, times = text.split('*')
  return '<{}></{}>'.format(tag, tag) * int(times)

