
def uncensor(string, vowels):
  stack  = [e for e in vowels][::-1];
  return "".join([letter if letter != "*" else stack.pop() for letter in string ]);

