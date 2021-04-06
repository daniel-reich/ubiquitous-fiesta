
def num_to_eng(n):
  if n == 0:
    return 'zero'
  one_to_nineteen = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'forteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
  twenty_to_ninety = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
  ans = []
  if n >= 100:
    ans += [one_to_nineteen[n//100]] + ['hundred']
  if n%100 >= 20:
    ans.append(twenty_to_ninety[(n%100)//10])
    if n%10 > 0:
      ans.append(one_to_nineteen[n%10])
  elif n%100 in one_to_nineteen:
    ans.append(one_to_nineteen[n%100])
  return ' '.join(ans)

