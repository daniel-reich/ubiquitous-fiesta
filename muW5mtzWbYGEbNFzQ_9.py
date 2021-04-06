
def BMR(person):
    x = [66.47, 13.75, 5.003, 6.755] if person["gender"] == "male" else [655.1, 9.563, 1.85, 4.676]
    return round((x[0] + person["weight"] * x[1] + person["size"] * x[2] - person['age'] * x[3]) * (1.025 + .175 * person["sport"]), 1)

