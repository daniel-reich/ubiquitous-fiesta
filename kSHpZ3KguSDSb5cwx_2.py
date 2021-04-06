
def dance_convert(pin):
    moves = ["Shimmy", "Shake", "Pirouette", "Slide",
             "Box Step", "Headspin", "Dosado", "Pop",
             "Lock", "Arabesque"]
​
    # Invalid input characters!
    invalidInputs = "ABDEFGHIJKLMNOPQRSTUVWXYZ+- abcdefghijklmnopqrstuvwxyz"
​
    # Check the inputs
    if len(list(filter(invalidInputs.__contains__, pin))) >= 1 or len(pin) < 4:
        return "Invalid input."
​
    digitsList = list(map(int, pin))
    result = []
    # Handle the input where all the digits are the same
    wrapAroundIndex = digitsList[0]
    if len(set(digitsList)) == 1:
        for i in range(4):
            numWrapAround = (((wrapAroundIndex - 0)) % len(moves) + 0)
            wrapAroundIndex += 1
            result.append(moves[numWrapAround])
    if len(result) == 4:
        return result
​
    # Normal digits where they are not the same
    for digit in digitsList:
        numWrapAround = (((digit - 0) + digitsList.index(digit)) % len(moves) + 0)
        result.append(moves[numWrapAround])
    return result

