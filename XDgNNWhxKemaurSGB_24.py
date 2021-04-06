
def k_th_binary_inlist(n, k):
  ones_in_bins = {}
​
  for num in range(0, 2**n):
    binn = bin(num)
    num_of_ones = str(binn).count('1')
    if num_of_ones in ones_in_bins.keys():
      ones_in_bins[num_of_ones].append(binn)
    else:
      ones_in_bins[num_of_ones] = [binn]
  
  binns = []
​
  for key in reversed(sorted(list(ones_in_bins.keys()))):
    for binary in ones_in_bins[key]:
      binns.append(binary)
​
  return binns[k-1]

