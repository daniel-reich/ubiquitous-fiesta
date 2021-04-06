
def wiggle_string(s):
  left_strings  = [" "*idx + s for idx in range(0 , len(s))]
  middle = [" " * (len(s)) + s]
  right_strings  = left_strings[::-1]
  return left_strings + middle + right_strings;

