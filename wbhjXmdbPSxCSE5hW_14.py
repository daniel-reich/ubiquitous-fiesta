
def sigilize(desire):
  a = [i for i in list(set(desire)) if i not in "aeiouAEIOU "]
  return "".join(sorted(a, key=lambda x:desire.rindex(x))).upper()

