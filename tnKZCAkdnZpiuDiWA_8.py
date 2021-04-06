
def flip_end_chars(txt):
    answer = "Incompatible."
    if len(txt) > 1:
      if type(txt) == str:
        answer = txt[-1] + txt[1:-1] + txt[0]
      
      if txt[-1] == txt[0]:
        answer = "Two's a pair."
      
    
    return answer

