
def min_swaps(string):
  alternative1 = "01" * len(string);
  alternative2 = "10" * len(string);
  return min(positional_differences(alternative1,string) , positional_differences(alternative2,string) );
  
def positional_differences(string,other):
  return sum([a!=b for a,b in zip(string , other)]);

