
animals = ["dog", "cat", "bat", "cock", "cow", "pig",
  "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
  "frog", "hen", "mole", "duck", "goat"]
​
def count_animals(txt):
  def occur(count,txt,animal):
    txt3 = txt
    for x in animal:
      txt3 = txt3.replace(x,"",1)
    if txt3 == txt:
      return count
    else:
      count += 1
      return occur(count,txt3,animal)
  print(txt)
  possible_words = []
  for animal in animals:
    if all(x in txt for x in animal):
        count = occur(0,txt,animal)
        for i in range(count):
          possible_words.append(animal)
  def outcome(txt,word,possible_words):
    count = 1
    for x in word:
      txt2 = txt.replace(x,"",1)
    for animal in possible_words:
      if all(x in txt2 for x in animal):
        for x in animal:
          txt2 = txt2.replace(x,"",1)
        count += 1
    return count
​
​
  numbers = []
  for word in possible_words:
    count = outcome(txt,word,possible_words)
    numbers.append(count)
  return max(numbers)

