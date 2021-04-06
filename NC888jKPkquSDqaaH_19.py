
import re
def clean_up(files, sort):
​
  seen = []
  results = []
​
  if sort == 'prefix':
​
    for idx, value in enumerate([re.search('[A-Za-z0-9]+', x).group() for x in files]):
​
      if idx == 0:
        seen.append(value)
        results.append([files[idx]])
​
      if value in seen and idx != 0:
        results[ [re.search('[A-Za-z0-9]+', x[0]).group() for x in results].index(value) ] += [files[idx]]
​
      elif value not in seen and idx != 0:
        seen.append(value)
        results.append([files[idx]])
​
    return results
​
​
  if sort == "suffix":
​
    for idx, value in enumerate([re.findall(r'[.](.+)', x)[0] for x in files]):
​
      if idx == 0:
        seen.append(value)
        results.append([files[idx]])
​
      if value in seen and idx != 0:
        results[ [re.findall(r'[.](.+)', x[0])[0] for x in results].index(value) ] += [files[idx]]
​
      elif value not in seen and idx != 0:
        seen.append(value)
        results.append([files[idx]])
​
    return results

