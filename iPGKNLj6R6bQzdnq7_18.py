
lst1 = ["John","Joe","Jack"]
lst2 = ["E","da","bit"]
lst3 = ["Metapod", "Magikarp", "Unown"]
template ="My {elem} are: {}, {} and {}."
​
​
​
print(template.format(*lst1, elem="friends"))
print(template.format(*lst2, elem="loves"))
print(template.format(*lst3, elem="pokemon"))

