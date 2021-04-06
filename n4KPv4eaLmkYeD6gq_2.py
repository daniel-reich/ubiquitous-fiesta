
def face_interval(num):
  return ':/' if type(num) is not list else ':)' if (max(num)-min(num)) in num else ':('

