
from collections import OrderedDict 
def keys_and_values(d):
  d_list = []
  for k, v in d.items():
    d_list.append({"key": k, "val": v})
  newlist = sorted(d_list, key=lambda k: k['key'])
  k_list = [x['key'] for x in newlist]
  v_list = [x['val'] for x in newlist]
  return [k_list, v_list]

