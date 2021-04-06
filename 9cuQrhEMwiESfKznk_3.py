
nums = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"twenty":20,"thirty":30,"forty":40,"fifty":50,"eighteen":18}
def eng2nums(s):
  numbers = s.split(" ")
  n = 0
  for i, word in enumerate(numbers):
    if "hundred" in numbers and i == 0:
      n += (100 * nums[numbers[0]])
    elif word in nums.keys():
      n += nums[word]
    elif word.endswith("teen"):
      n+= nums[word.replace("teen",'')] + 10
    elif word.endswith("ty"):
      n+= nums[word.replace("ty",'')] * 10
  return n

