
def over_twenty_one(lst):
  lst_value = [10 for nums in lst if nums in ["K", "Q", "J"]]
  num_value = [num for num in lst if num in range(1,11)]
  if "A" in lst and (sum(lst_value) + sum(num_value)) <= 20:
    total = sum(lst_value) + sum(num_value) + 1
  elif "A" in lst and (sum(lst_value) + sum(num_value)) <= 10:
    total = sum(lst_value) + sum(num_value) + 11
  else:
    total = sum(lst_value) + sum(num_value)
  return total > 21

