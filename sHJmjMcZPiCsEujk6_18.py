
def pilish_string(txt):
  pi_digits = '314159265358979'
  digits_sum = 0
  result = []
  for digit in pi_digits:
    if digits_sum >= len(txt):
      break
    cur_digit = int(digit)
    split_word = txt[digits_sum:digits_sum + cur_digit]
    if cur_digit > len(split_word):
      split_word = ''.join(
        [split_word, split_word[-1] * (cur_digit - len(split_word))]
      )
    result.append(split_word)
    digits_sum += cur_digit
  return ' '.join(result)

