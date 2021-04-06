
def closest_palindrome(num):
    i = 0
    while True:
        first_candidate, second_candidate = num - i, num + i
        if str(first_candidate) == str(first_candidate)[::-1]:
            return first_candidate
        elif str(second_candidate) == str(second_candidate)[::-1]:
            return second_candidate
        else:
            i += 1

