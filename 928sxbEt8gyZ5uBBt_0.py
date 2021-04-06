
def wurstIsBetter(str):
    sausages = ["Kielbasa", "Chorizo", "Moronga", "Salami", "Sausage", "Andouille", "Naem", "Merguez", "Gurka", "Snorkers", "Pepperoni"]
    return " ".join(["Wurst" if x.title() in sausages else x for x in str.split() ])

