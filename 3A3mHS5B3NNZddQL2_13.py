
def interview(times, total):
    fmt = ["very easy", "very easy", "easy", "easy", "medium", "medium", "hard", "hard"]
    maxtimes = {
        "very easy": 5,
        "easy": 10,
        "medium": 15,
        "hard": 20
    }
​
    asserts = [not t > maxtimes[i] for t, i in zip(times, fmt)]
​
    if total <= 120 and all(asserts) and len(times) == len(fmt):
        return "qualified"
    return "disqualified"

