
def get_xp(d):
    scale = {
        "Very Easy": 5,
        "Easy": 10,
        "Medium": 20,
        "Hard": 40,
        "Very Hard" : 80
    }
    
    score = 0
    
    if d:
        for category in ("Very Easy", "Easy", "Medium", "Hard", "Very Hard"):
            if category in d.keys():
                value = d.get(category, 0)
                if value > 0:
                    score = score + (value * scale.get(category))
​
    return "{}XP".format(score)
​
​
if __name__ == "__main__":
    print(get_xp({
    "Very Easy" : 89,
    "Easy" : 77,
    "Medium" : 30,
    "Hard" : 4,
    "Very Hard" : 1
    }))

