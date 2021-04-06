
def fruit_salad(fruits):
  final_str = ''
  split_fruits = []
  for f in fruits:
    first_half, second_half = f[:len(f)//2],f[len(f)//2:]
    split_fruits.append(first_half)
    split_fruits.append(second_half)
  sort_split_fruits = sorted(split_fruits, key=str.lower)
  for split in sort_split_fruits:
    for s in split:
      final_str = ''.join((final_str, s))
      
  return final_str

