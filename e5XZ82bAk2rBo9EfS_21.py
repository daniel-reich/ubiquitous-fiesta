
def bed_time(*times):
  def sub(data):
    [h1,m1],[h2,m2] = data[0].split(":"),data[1].split(":")
    m = int(m1)-int(m2)
    h = int(h1)-int(h2)+m//60
    return "{:0>2}:{:0>2}".format(h%24,m%60)
​
  return [sub(data) for data in times]

