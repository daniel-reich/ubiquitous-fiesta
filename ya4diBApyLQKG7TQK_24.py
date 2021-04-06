
def validate_relationships(txt):
  op=''.join(i if i in '><=' else ' ' for i in txt).split()
  for i in range(len(op)):
    if op[i]=='=':
      op[i]='=='
  txt=''.join(i if i not in '><=' else ' ' for i in txt).split()
  return eval('{}'.join(txt).format(*op))

