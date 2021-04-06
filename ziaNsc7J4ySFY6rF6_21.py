
def will_fit(holds, cargo):
    cargo_space = {'S': 50, 'M': 100, 'L': 200}
    test = dict(zip(holds, cargo))
    for key in test.keys():
        if cargo_space[key] < test[key]:
            return False
        else:
            return True

