
def title_to_number(s):
  if not s:
    return 0
  return 1 + ord(s[-1]) - ord('A') + 26 * title_to_number(s[:-1])

