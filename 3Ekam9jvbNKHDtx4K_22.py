
def line_length(dot1, dot2):
  return round(sum([(dot1[i]-dot2[i])**2 for i in range(len(dot1))])**0.5,2)

