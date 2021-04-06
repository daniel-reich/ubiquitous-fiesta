
import re
animals = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]
def fauna_number(txt):
  res = []
  for x, word in enumerate(re.split(",| ", txt)):
    for animal in animals:
      if word == animal:
        res.append((animal, re.split(",| ", txt)[x-1]))
  return res

