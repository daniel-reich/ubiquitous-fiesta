
def digit_occurrences(start, end, digit):
    interval = range(start, end + 1)
    count = 0
    for num in interval:
        num_string = str(abs(num))
        for letter in num_string:
            if letter == str(digit):
                count += 1
            continue
    return count

