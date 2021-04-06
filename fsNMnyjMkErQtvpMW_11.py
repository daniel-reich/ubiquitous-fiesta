
def holey_sort(lst):
  
  Values = lst
  
  # Establishing Number of Holes in Each Item of Values
  
  Occurrences = []
  
  VC = 0
  VL = len(Values)
  
  while (VC < VL):
    
    Text = str(Values[VC])
    Holes = 0
    
    Count_Zero = Text.count("0")
    Count_Four = Text.count("4")
    Count_Six = Text.count("6")
    Count_Eight = Text.count("8")
    Count_Nine = Text.count("9")
    
    Holes += Count_Zero
    Holes += Count_Four
    Holes += Count_Six
    Holes += Count_Eight
    Holes += Count_Eight
    Holes += Count_Nine
    
    Occurrences.append(Holes)
    VC += 1
  
  # Trimming Occurrences to Unique Values
  
  Occurrences = set(Occurrences)
  Occurrences = list(Occurrences)
  Occurrences = sorted(Occurrences)
  
  # Performing Sort
  
  Filtered = []
  Filtered.append("X")
  FL = len(Filtered)
  
  OC = 0
  OL = len(Occurrences)
  
  VC = 0
  VL = len(Values)
  
  while (FL <= VL) and (OC < OL):
    
    Target = Occurrences[OC]
    
    Item = Values[VC]
    Text = str(Values[VC])
    
    Holes = 0
    
    Count_Zero = Text.count("0")
    Count_Four = Text.count("4")
    Count_Six = Text.count("6")
    Count_Eight = Text.count("8")
    Count_Nine = Text.count("9")
    
    Holes += Count_Zero
    Holes += Count_Four
    Holes += Count_Six
    Holes += Count_Eight
    Holes += Count_Eight
    Holes += Count_Nine
    
    if (Holes == Target):
      Filtered.append(Item)
      VC += 1
    else:
      VC += 1
    
    if (VC == VL):
      VC = 0
      OC += 1
  
  # Establishing and Giving Answer
  Filtered = Filtered[1:]
  return Filtered

