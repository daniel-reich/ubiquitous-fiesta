
Stem_Dict = {1984: "Wood", 1985: "Wood", 1986: "Fire", 1987: "Fire", 1988: "Earth", 1989: " Earth", 1990: "Metal", 1991: "Metal", 1992: "Water", 1993: "Water"}
Branch_Dict = {1984: "Rat", 1985: "Ox", 1986: "Tiger", 1987: "Rabbit", 1988: "Dragon", 1989: "Snake", 1990: "Horse", 1991: "Sheep", 1992: "Monkey", 1993: "Rooster", 1994: "Dog", 1995: "Pig"}
​
def sexagenary(year = 1948):
​
    My_Zodiac = ""
    for key, item in Branch_Dict.items():
        for k, i in Stem_Dict.items():
            if(key - year) % 12 == 0 and (k - year) % 10 == 0:
                My_Zodiac += (i + " " + item)
​
    return My_Zodiac

