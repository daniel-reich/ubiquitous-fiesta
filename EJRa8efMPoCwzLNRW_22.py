
def IsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
​
def dakiti(sentence):
  list1 = sentence.split()
  print(list1)
  list2 = []
  num = 0
  for i in range(len(sentence)):
    if IsInt(sentence[i]):
      num = num + 1
      list2.append(sentence[i])
  list2, list1 = zip(*sorted(zip(list2, list1)))
  phrase = ",".join(list1)
  for i in range(int(num)):
    #print("ran")
    phrase = phrase.replace(str(num)," ")
    num = num - 1
  list1 = list(phrase)
  list1[:] = (value for value in list1 if value != " ")
  phrase = "".join(list1)
  phrase = phrase.replace(","," ")
  return phrase

