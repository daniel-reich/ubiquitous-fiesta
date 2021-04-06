
def same_letter_pattern(txt1, txt2):
  return len(set(txt1)) == len(set(zip(txt1, txt2))) if len(txt1)==len(txt2) else False

