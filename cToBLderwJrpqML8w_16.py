
def champions(teams):
  lst = [i for i in teams if (i['wins']*3)+i['draws']==max([(3*j['wins'])+j['draws'] for j in teams])]
  if len(lst)==1:
    return lst[0]['name']
  else:
    return [i['name'] for i in lst if i['scored']-i['conceded']==max([j['scored']-j['conceded'] for j in lst])][0]

