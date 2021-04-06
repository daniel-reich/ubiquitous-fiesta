
def return_end_of_number(num):
  d = {"1": "-ST", "2": "-ND", "3": "-RD", "11": "-TH", "12": "-TH", "13": "-TH"}
  if num < 10:
    return str(num) + "-TH" if str(num)[-1] not in d.keys() else str(num) + d[str(num)[-1]]
  return str(num) + "-TH" if str(num)[-2:] not in d.keys() and str(num)[-1] not in d.keys() else \
    str(num) + d[str(num)[-2:]] if str(num)[-2:] in d.keys() else str(num) + d[str(num)[-1]]

