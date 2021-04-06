
class Calculator:
  for x,y in {'add':'+','subtract':'-','multiply':'*','divide':'/'}.items():
    exec('def ' + x + '(self, x, y): return x' + y + 'y')

