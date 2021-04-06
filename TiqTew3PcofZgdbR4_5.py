
def bitwise_and(n1, n2):
  n1 = list(bin(n1))[2:]
  n2 = list(bin(n2))[2:]
  while len(n1) < len(n2):
    n1.insert(0, "0")
  while len(n2) < len(n1):
    n2.insert(0, "0")
  return int("".join(["1" if n1[i] == "1" and n2[i] == "1" else "0" for i in range(len(n1))]), 2)
​
def bitwise_or(n1, n2):
  n1 = list(bin(n1))[2:]
  n2 = list(bin(n2))[2:]
  while len(n1) < len(n2):
    n1.insert(0, "0")
  while len(n2) < len(n1):
    n2.insert(0, "0")
  return int("".join(["1" if n1[i] == "1" or n2[i] == "1" else "0" for i in range(len(n1))]), 2)
​
def bitwise_xor(n1, n2):
  n1 = list(bin(n1))[2:]
  n2 = list(bin(n2))[2:]
  while len(n1) < len(n2):
    n1.insert(0, "0")
  while len(n2) < len(n1):
    n2.insert(0, "0")
  return int("".join(["1" if (n1[i] == "1" or n2[i] == "1") and n1[i] != n2[i] else "0" for i in range(len(n1))]), 2)

