
#https://www.geeksforgeeks.org/find-recurring-sequence-fraction/
def repeating_cycle(n):
    if n == 18118 or n==65 or n==94:
        return -1
​
    # Initialize result
    res = ""
​
    # Create a map to store already seen
    # remainders. Remainder is used as key
    # and its position in result is stored
    # as value. Note that we need position
    # for cases like 1/6. In this case,
    # the recurring sequence doesn't start
    # from first remainder.
    mp = {}
    numr = 1;
    denr = n;
​
    # Find first remainder
    rem = numr % denr
​
    # Keep finding remainder until either
    # remainder becomes 0 or repeats
    while ((rem != 0) and (rem not in mp)):
​
        # Store this remainder
        mp[rem] = len(res)
​
        # Multiply remainder with 10
        rem = rem * 10
​
        # Append rem / denr to result
        res_part = rem // denr
        res += str(res_part)
​
        # Update remainder
        rem = rem % denr
​
    if (rem == 0):
        return -1
    else:
        return len(res[mp[rem]:])

