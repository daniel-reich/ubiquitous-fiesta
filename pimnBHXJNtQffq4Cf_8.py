
def mapping(letters):
  mp = {};
  for i in range(len(letters)):
    mp.update({
      letters[i] : chr(ord(letters[i])-32)
    });
  return mp;

