
def is_valid_hex_code(txt):
  return (txt[0]=='#') and (len(txt)==7) and all([x in '0123456789abcdef' for x in txt.lower()[1:]])

