
def encrypt(word):
  step1 = word[::-1]
  step2 = "".join([i if i not in "aeou" else str("aeou".index(i)) for i in step1])
  step3 = step2 + "aca"
  return step3

