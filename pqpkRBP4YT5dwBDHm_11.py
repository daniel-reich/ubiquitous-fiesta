
def show_the_love(lst):
  reduced =  [num - (num * .25) for num in lst ]
  total_deduction = sum(num * .25 for num in lst)
  reduced[reduced.index(min(reduced))] = reduced[reduced.index(min(reduced))] + total_deduction
  lst = reduced
  return [int(str(num)[:len(str(num))-2]) if str(num)[-1] == '0' and str(num)[-2] == '.' else num for num in lst  ]

