
def parallel_resistance(lst):
  a=sum([1/i for i in lst])
  return round(1/(a),1)

