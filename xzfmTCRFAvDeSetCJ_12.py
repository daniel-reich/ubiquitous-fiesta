
dic1 = {"name": "Mary","name1":"May","sentence1":"like","sentence2":"don't like"}
dic2 = {"name": "Eda","name1":"Bit","sentence1":"love","sentence2":"don't love"}
dic3 = {"name": "Pidgey","name1":"Rattata","sentence1":"have a","sentence2":"don't have a"}
​
template = "I {sentence1} {name}, I {sentence2} {name1}."
template.format(**dic1)
template.format(**dic2)
template.format(**dic3)

