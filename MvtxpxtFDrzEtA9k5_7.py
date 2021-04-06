
def palindrome_descendant(num):
  print(num)
  num = str(num)
  first_num = num[:len(num)//2]
  second_num = num[len(num)//2:]
  second_num = second_num[::-1]
  if(first_num == second_num):
    print(True)
    return True
  elif (len(num) == 2):
    print(False)
    return False
  elif(len(num) % 2 == 1):
    return False
  else:
    new_num = ""
    for i in range(0, len(num), 2):
      new_num = new_num + str(int(num[i]) + int(num[i+1]))
    return palindrome_descendant(int(new_num))

