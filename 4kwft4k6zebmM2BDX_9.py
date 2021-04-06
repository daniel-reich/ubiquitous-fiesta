
def chi_squared_test(data):
  ls1,ls2=[],[]
  alpha1=6.635
  alpha5=3.841
  lsE=sum(data['E'])
  lsT=sum(data['T'])
  for k,v in data.items():
      ls1.append(v[0])
      ls2.append(v[1])
  lst1=sum(ls1)
  lst2=sum(ls2)
  ColT=lst1+lst2
  Ed2=(lsE*lst1)/ColT
  Edhalf=(lsE*lst2)/ColT
  EdRowT=Ed2+Edhalf
  Tut2=(lsT*lst1)/ColT
  Tuthalf=(lsT*lst2)/ColT
  TutRowT=Tut2+Tuthalf
  Tothalf=Edhalf+Tuthalf
  ki1=((ls1[0]-Ed2)**2)/Ed2
  ki2=((ls2[0]-Edhalf)**2)/Edhalf
  ki3=((ls1[1]-Tut2)**2)/Tut2
  ki4=((ls2[1]-Tuthalf)**2)/Tuthalf
  kisq=ki1+ki2+ki3+ki4
  if kisq>alpha1:
      return [round(kisq,1),"Edabitin effectiveness = 99%"]
  elif kisq<alpha1 and kisq>alpha5:
      return [round(kisq,1),'Edabitin effectiveness = 95%']
  elif kisq<alpha5:
      return [round(kisq,1),"Edabitin is ininfluent"]
  else:
      pass

