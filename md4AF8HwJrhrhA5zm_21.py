
colours = ["red", "red-orange", "orange", "yellow-orange", 
           "yellow", "yellow-green",  "green", "blue-green", 
           "blue", "blue-violet", "violet", "red-violet"];
             
def colour_harmony(anchor, combination):
  anchor_idx = colours.index(anchor);
  shifted  = colours[anchor_idx:] + colours[:anchor_idx];
  
  if (combination  == "complementary"):
    return set(shifted[::12//2]);
    
  if (combination  == "triadic"):
    return set(shifted[::12//3]);
    
  if (combination  == "square"):
    return set(shifted[::12//4]);
    
  if (combination  == "analogous"):
    return set([shifted[-1] , shifted[0]  , shifted[1]] );
    
  if (combination  == "split_complementary"):
    return set([shifted[0], shifted[5] , shifted[7]]);
    
  if (combination  == "rectangle"):
    return set([shifted[0], shifted[2] , shifted[6] , shifted[8]]);
    
  else :
    return "sorry , provided combination is unknown anyway";

