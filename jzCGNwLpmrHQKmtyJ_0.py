
def parityAnalysis(num):
  digit_sum = sum(int(i) for i in str(num))
  return digit_sum%2 == num%2

