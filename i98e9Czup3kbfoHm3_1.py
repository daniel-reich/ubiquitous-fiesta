
def text_to_number_binary(txt):
  lista = []
  for i in txt.split():
    if i.lower() == "zero":
      lista.append("0")
    elif i.lower() == "one":
      lista.append("1")
  divisor = len(lista) - len(lista) % 8
  return "".join(lista) if len(lista) % 8 == 0 else "".join(lista[:divisor])

