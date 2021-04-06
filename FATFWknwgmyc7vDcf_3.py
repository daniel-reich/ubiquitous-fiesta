
import re
def small_favor(sentence):
  under25=r"(\d\d[./]\d\d[./]|(January|February|March|April|May|June|July|August|September|October|November|December), \d\d. )[0-1][0-9](?![/0-9.|][0-9])|(\d\d[./]\d\d[./]|(January|February|March|April|May|June|July|August|September|October|November|December), \d\d. )[2][0-4](?![/0-9.|][0-9])"
  overand25=r"(\d\d[./]\d\d[./]|(January|February|March|April|May|June|July|August|September|October|November|December), \d\d. )[3-9][0-9](?![/0-9.|][0-9])|(\d\d[./]\d\d[./]|(January|February|March|April|May|June|July|August|September|October|November|December), \d\d. )[2][5-9](?![/0-9.|][0-9])"
  if len(re.findall(under25,sentence))>0:
    for x in range(0,len(re.findall(under25,sentence))):
      date=re.search(under25,sentence).group()
      sentence=re.sub(under25,date[0:len(date)-2]+"20"+date[len(date)-2:len(date)],sentence, count=1)
  if len(re.findall(overand25,sentence))>0:
    for x in range(0,len(re.findall(overand25,sentence))):
      date=re.search(overand25,sentence).group()
      sentence=re.sub(overand25,date[0:len(date)-2]+"19"+date[len(date)-2:len(date)],sentence, count=1)
  return sentence

