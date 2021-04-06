
def text_to_num(phone):
  noletters = phone.translate(str.maketrans( "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "2223334445556667777888999922233344455566677778889999"))
  return noletters

