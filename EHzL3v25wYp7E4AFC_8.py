
def can_build(input, output):
    return all([input.count(letter) >= output.count(letter) for letter in output])

