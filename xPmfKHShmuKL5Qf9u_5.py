
def scale_tip(lst):
  return ['left','balanced','right'][sum([sum(lst[:lst.index('I')])<sum(lst[lst.index('I')+1:]),sum(lst[:lst.index('I')])<=sum(lst[lst.index('I')+1:])])]

