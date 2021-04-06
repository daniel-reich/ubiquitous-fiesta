
def longest_7segment_word(lst):
  return max([x for x in lst if not set(x) & set("kmvwx")], key=len, default="")

