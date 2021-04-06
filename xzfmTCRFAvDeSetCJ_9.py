
dic1 = {"one": "like", "two": "Mary", "three": "May"}
dic2 = {"one": "love", "two": "Eda", "three": "Bit"}
dic3 = {"one": "have a", "two": "Pidgey", "three": "Rattata"}
​
template = "I {one} {two}, I don't {one} {three}."
​
template.format(**dic1)
template.format(**dic2)
template.format(**dic3)

