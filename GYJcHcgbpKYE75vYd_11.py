
def return_end_of_number(num):
  return "{}-{}".format(num, "TSNRHTDD"[(num//10%10!=1)*(num%10<4)*num%10::4])

