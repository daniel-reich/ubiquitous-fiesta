
def mode(nums):
  dic, max, res = {}, 0, []
  for num in nums:
    k = str(num)
    if k in dic: dic[k] += 1
    else: dic[k] = 1
  for v in dic.values():
    if v > max: max = v
  for k, v in dic.items():
    if v == max: res.append(int(k))
  return sorted(res)

