
def char_appears(sentence, char):
  char = char.lower();
  ret = []
  for word in sentence.lower().split():
    count = 0;
    for c in word:
      if c == char:
        count += 1;
    ret.append(count)
  return ret;

