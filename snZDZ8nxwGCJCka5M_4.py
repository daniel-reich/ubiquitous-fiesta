
def pyramidal_string(string, _type):
  if string == "":
    return []
​
  if _type == "REV":
    string = putar(string)
​
  data = []
  x = 0
  while x <= len(string) - 1:
    if _type == "REV":
      data += [ putar(pisah_kata(string[:x+1])) ]
    else:
      data += [ pisah_kata(string[:x+1]) ]
    string = string[x+1::]
    x += 1
​
  if len(string) == 0:
    return putar_arr(data) if _type == "REV" else data
  else:
    return "Error!"
​
def putar_arr(data):
  hasil = []
  for i in data:
    hasil = [i] + hasil
  return hasil
​
def putar(string):
  data = ""
  for i in string:
    data = i + data
  return data
​
def pisah_kata(string):
  data = []
  for i in string:
    data += [i]
  return " ".join(data)

