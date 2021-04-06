
def digital_vowel_ban(n, l):
  dic = {'0':'zero','1':'one', '2':'two','3':'three', '4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}    
  try:
    return int("".join([i for i in str(n) if l not in dic[i]]))
  except:
    return "Banned Number"

