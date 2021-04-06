
nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def num_to_eng(n):
  if n > 100:
    return nums[n//100] + " hundred " + num_to_eng(n%100)
  if n < 20:
    return nums[n]
  if n % 10 == 0:
    return tens[n//10-2]
  return tens[n//10-2] + " " + nums[n%10]

