
def is_repdigit(num):
 num = str(num)
 return True if num.count(num[0]) == len(num) or num == "0" else False

