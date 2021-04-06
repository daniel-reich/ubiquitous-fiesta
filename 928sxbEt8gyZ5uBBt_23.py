
convert = [
    "kielbasa",
    "chorizo",
    "moronga",
    "salami",
    "sausage",
    "andouille",
    "naem",
    "merguez",
    "gurka",
    "snorkers",
    "pepperoni"
]
​
def wurst_is_better(txt):
    result = []
    for word in txt.split():
        is_plural = word[-1] == "s"
        if word.lower() in convert or is_plural and word[:-1].lower() in convert:
            result.append("Wursts" if is_plural else "Wurst")
        else:
            result.append(word)
    return " ".join(result)

