
import json
​
def navigate(roads, startingNode, endingNode):
  c=json.loads(roads)
​
  pos={startingNode:{'distance':0,'path':[startingNode]}}
    
  while endingNode not in pos:
    print(startingNode, endingNode,pos)
    posnew={}
    for x in c['edges']:
      s=x['source'] # value in source
      t=x['target'] # value in target
      d=x['metadata']['distance'] # distance
      if s in pos and  t not in pos:
        tmp={'distance':pos[s]['distance']+d,
        'path':pos[s]['path'][:]}
        tmp['path'].append(t)
        posnew.update({t:tmp} )
        
      t=x['source'] # value in source
      s=x['target'] # value in target
      if s in pos and  t not in pos:
        tmp={'distance':pos[s]['distance']+d,
        'path':pos[s]['path'][:]}
        tmp['path'].append(t)
        posnew.update({t:tmp} ) 
    pos=posnew
    
  print(pos[endingNode])
  return(pos[endingNode])

