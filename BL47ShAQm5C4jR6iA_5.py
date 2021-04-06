
def third_most_expensive(dct):
    if(len(dct) > 2):
      return list(sorted(dct.items(), key=lambda i: i[1])[-3])[0]
    return 0
​
​
print(third_most_expensive({"Jack": 3, "Alice": 4, "Bob": 2}))

