
def split_n_cases(txt, cases):
  if len(txt) % cases != 0:
    return ["Error"]
  num_sections = len(txt) // cases
  return [txt[i: i + num_sections] for i in range(0, len(txt), num_sections)]

