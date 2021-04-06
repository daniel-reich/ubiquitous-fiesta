
def first_and_last(s):
  return ["".join(x for x in sorted(c for c in s)),"".join(x for x in reversed(sorted(c for c in s)))]

