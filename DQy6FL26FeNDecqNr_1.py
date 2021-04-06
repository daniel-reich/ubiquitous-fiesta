
def correct_stream(user, correct):
​
    return [1 if typed == expected else -1
            for typed, expected in zip(user, correct)]

