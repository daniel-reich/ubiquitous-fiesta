
def sweetest_icecream(lst):
 dic={"Plain":0,"Vanilla":5,"ChocolateChip":5,"Strawberry":10,"Chocolate":10}
 lst_1=[]
 for i in lst:
  lst_1.append(dic[i.flavor]+i.num_sprinkles)
 return max(lst_1)

