
def face_interval(num):
  return (":)" if max(num) - min(num) in num else ":(") if type(num) == list else ":/"

