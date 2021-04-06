
def golf_score(course, result):
​
    scores = {"eagle": -2,
              "birdie": -1,
              "par": 0,
              "bogey": 1,
              "double-bogey": 2}
​
    return sum([a + scores[b] for a, b in zip(course, result)])

