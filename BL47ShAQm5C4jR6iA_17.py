
def third_most_expensive(dct):
  lst = sorted([dct[i] for i in dct])
  return [i for i in dct if dct[i]==lst[-3]][0] if len(dct)>=3 else False

