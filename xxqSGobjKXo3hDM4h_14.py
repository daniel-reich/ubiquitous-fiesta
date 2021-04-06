
import re
def ing_extractor(string):
  end = r'ing$|ING$'
  def valid(s):
    if bool(re.search(end,s)) == False:
      return False
    else:
      return bool(re.search(r'[aeiouAEIOU]|\W',re.sub(end,'',s)))
    
  return list(filter(lambda x: valid(x),re.findall(r'\S+',string)))

