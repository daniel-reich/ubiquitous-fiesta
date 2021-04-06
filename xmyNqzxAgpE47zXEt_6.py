
def is_alphabetically_sorted(sentence):
  s=sentence.replace('.', '')
  s=s.split(' ')
  lst=[]
  string=''
  one=s[0]
  two=s[1]
  three=s[2]
  try:
    four=s[3]
  except:
    four='' 
  try:
    five=s[4]
  except:
    five=''
  try:
    six=s[5]
  except:
    six=''
  try:
    seven=s[6]
  except:
    seven=''
  try:
    eight=s[7]
  except:
    eight=''
  try:
    nine=s[8]
  except:
    nine=''
  try:
    ten=s[9]
  except:
    ten=''
  one=one.lower()
  two=two.lower()
  three=three.lower()
  four=four.lower()
  five=five.lower()
  six=six.lower()
  seven=seven.lower()
  eight=eight.lower()
  nine=nine.lower()
  ten=ten.lower()
  for i in one:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==one and len(string) > 2):
    return True
  string=''
  lst=[]
  for i in two:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==two and len(string) > 2):
    return True
  string=''
  lst=[]
  for i in three:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==three and len(string) > 2):
    return True
  string=''
  lst=[]
  for i in four:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==four and len(string) > 2):
    return True
  string=''
  lst=[]
  for i in five:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==five and len(string) > 2):
    return True
  string=''
  lst=[]
  for i in six:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==six and len(string) > 2):
    return True
  string=''
  lst=[]
  for i in seven:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==seven and len(string) > 2):
    return True
  string=''
  lst=[]
  for i in eight:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==eight and len(string) > 2):
    return True
  string=''
  lst=[]
  for i in nine:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==nine and len(string) > 2):
    return True
  string=''
  lst=[]
  for i in ten:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==ten and len(string) > 2):
    return True
  string=''
  lst=[]
  return False

