
def ranged_reversal(lst, start, finish):
  subsection = lst[start:(finish+1)]
  revsubsection = subsection[::-1]
  newlist = lst[:start]+revsubsection+lst[(finish+1):]
  return newlist

