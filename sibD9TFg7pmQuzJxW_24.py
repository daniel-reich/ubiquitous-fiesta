
def stem_plot(arr):
  arr.sort()
  stem = ''
  leaf = ''
  resultarr = []
  for i in arr:
    if len(str(i)) == 1: i = '0' + str(i)
​
    if leaf == str(i)[:-1]: stem = stem + " " + str(i)[-1]
​
    elif leaf != '':
      resultarr.append(leaf + " | " + stem)
      leaf = str(i)[:-1]
      stem = str(i)[-1]
    
    else:      
      leaf = str(i)[:-1]
      stem = str(i)[-1]
  resultarr.append(leaf + " | " + stem)
  return resultarr

