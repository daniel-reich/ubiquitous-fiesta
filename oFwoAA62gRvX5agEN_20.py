
def knapsack(capacity, items):
  import pandas as pd
  i=0
  df=pd.DataFrame(columns=['name','weight','value'])
  for item in items:
    df.loc[i,'name']=item['name']
    df.loc[i,'weight']=item['weight']
    df.loc[i,'value']=item['value']
    i+=1
  if(len(items)>4):
    df=df.sort(['value'],ascending=False).reset_index()
  else:
    df=df.sort(['weight']).reset_index()
  items_, items1,weight, value =[],[],0,0
  for i in range (df.shape[0]):
    if (weight+df.loc[i,'weight']<=capacity):
      items_.append({'name':df.loc[i,'name'],'weight':df.loc[i,'weight'],'value':df.loc[i,'value']})
      weight +=df.loc[i,'weight']
      value +=df.loc[i,'value']
  for item in items:
    if (item in items_):
      items1.append(item)
  return {'capacity': capacity, 'items': items1, 'weight': weight, 'value': value}

