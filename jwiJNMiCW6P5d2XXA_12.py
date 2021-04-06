
def does_rhyme(txt1, txt2):
​
  return (txt1.lower()[0:-1]).endswith(txt2.lower()[-3:-1])

