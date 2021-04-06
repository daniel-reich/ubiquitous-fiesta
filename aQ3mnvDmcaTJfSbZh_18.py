
import pandas as pd
def bw_transform(text):
  l_w=[l for l in text.strip() ]
  y=l_w.copy()
  con=[y]
  for i in range(len(text)-1):
    l_w.insert(len(l_w),l_w[0])
    l_w=l_w[1:]
    v=l_w.copy()
    con.append(v)
  sort=sorted([''.join( l for l in lst )for lst in con ])
  complete=[[l for l in i] for i in sort]
  df=pd.DataFrame(complete).sum()
  return df.iloc[len(text)-1]

