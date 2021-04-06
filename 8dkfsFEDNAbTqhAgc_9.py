
def division(a, b):
  if a%b==0:
    return str(a/b)
  else:
    result = ""
    result += str(a // b)
    result += "."
    A = []
    while a:
      r = a % b
      if r == 0:
        for x in A:
          result += str(x[-1])
        break
      else:
        a = r*10
        q = a // b
        if [a, q] not in A:
          A.append([a, q])
        elif [a, q] in A:
          index = A.index([a, q])
          for x in A[:index]:
            result += str(x[-1])
          result += "("
          for y in A[index:]:
            result += str(y[-1])
          result += ")"
          break
    return result

