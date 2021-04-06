
def shared_letters(a, b):
 output=''
 # make case insensitive
 a_lower=a.lower()
 b_lower=b.lower()
 # go through a
 for i in range(0,len(a_lower)):
  # if a[i] in b and not in output
  if a_lower[i] in b_lower and a_lower[i] not in output:
   # add to output
   output+=a_lower[i]
 #print(output)
 # sort output
 output_sorted=sorted(output)
 output_str=''.join(output_sorted)
 return output_str

