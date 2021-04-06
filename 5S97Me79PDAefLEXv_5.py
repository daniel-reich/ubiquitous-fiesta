
def lambda_to_def(code):
  name = code.split(" ")[0]
  args = code.split("= lambda ",1)[1]
  args = ": ".join(args.split(": ")[:-1])
  execution = code.split(": ")[-1]
  
  return "def "+name+"("+args+")"+":\n\treturn "+execution

