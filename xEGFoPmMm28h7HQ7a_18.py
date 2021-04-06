
def letter_combinations(digits):
  phonelist=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
  combinations=[]
  try:
    firstnumber=phonelist[int(digits[0])-2]
    secondnumber=phonelist[int(digits[1])-2]
    thirdnumber=phonelist[int(digits[2])-2]
    for i in range(0,len(firstnumber)):
      for j in range (0,len(secondnumber)):
        for k in range (0,len(thirdnumber)):
          combinations.append("{}{}{}".format(firstnumber[i],secondnumber[j],thirdnumber[k]))
    return combinations
  except:
    firstnumber=phonelist[int(digits[0])-2]
    secondnumber=phonelist[int(digits[1])-2]
    for i in range(0,len(firstnumber)):
      for j in range (0,len(secondnumber)):
          combinations.append("{}{}".format(firstnumber[i],secondnumber[j]))
    return combinations

