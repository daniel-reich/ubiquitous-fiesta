
def handle_two_digits(s):
  if not s: return 0
  ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'] 
  tens = ['zero', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
  if ' ' in s:
    x,y = s.split(' ')
    return 10 * tens.index(x) + ones.index(y)
  if s in ones:
    return ones.index(s)
  return 10 * tens.index(s)
  
def eng2nums(s):
  if ' hundred' in s:
    x,y = s.split(' hundred')
    return 100 * handle_two_digits(x) + handle_two_digits(y.lstrip())
  return handle_two_digits(s)

