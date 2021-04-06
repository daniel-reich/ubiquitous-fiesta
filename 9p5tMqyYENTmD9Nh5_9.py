
def is_valid_hex_code(txt):
  if txt[0]!='#' or len(txt)!=7: return False
  return set(txt[1:].lower())<=({str(i) for i in range(10)}|{chr(i) for i in range(ord("a"),ord('f')+1)})

