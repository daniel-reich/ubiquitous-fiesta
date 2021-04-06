
def champions(teams):
    return sorted(teams, key=lambda item: (item["wins"]*3 + item["draws"]*1, item["scored"]-item["conceded"]))[-1]["name"]

