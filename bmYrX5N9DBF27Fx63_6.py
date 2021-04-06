
def greatest_impact(lst):
  lst1=[list(i) for i in zip(*lst)]
  final=sorted([["Weather",sum(lst1[1])/10],["Meals",sum(lst1[2])/3],["Sleep",sum(lst1[3])/10]],key=lambda x: (x[1]))
  if sum(lst1[0])/10<3.0:
      return final[0][0]
  return "Nothing"

