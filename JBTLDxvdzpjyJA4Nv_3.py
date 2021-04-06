
def super_reduced_string(s):
  stack=[]
  for x in s:
    if stack==[] or stack[-1]!=x:
      stack.append(x)
    else:
      stack.pop()
  return ''.join(stack) if stack!=[] else 'Empty String'

