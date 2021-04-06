
def binary(decimal):
    lst = []
    ques = decimal
    if ques == 0:
      return '0'
    while ques != 0:
        rem = ques % 2
        ques = ques // 2
        lst.append(rem)
​
​
    lst.reverse()
    str_lst = ""
    for item in lst:
           str_lst += str(item)
    return str_lst

