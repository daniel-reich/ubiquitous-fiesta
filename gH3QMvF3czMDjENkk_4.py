
def remove_letters(letters, word):
  result = []
  remove = list(word)
  for lt in letters:
    passed = True
    for rm in remove:
      if lt == rm:
        remove.remove(rm)
        passed = False
        break
    if passed:
      result.append(lt)
  return result

