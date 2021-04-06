
lst1 = ['John','Joe', 'Jack']
lst2 = ['E', 'da', 'bit']
lst3 = ["Metapod","Magikarp","Unown"]
​
template = "My {elem} are: {0}, {1} and {2}."
print(template.format(*lst1, elem = 'friends'))
print(template.format(*lst1, elem = 'loves'))
print(template.format(*lst1, elem = 'pokemon'))

