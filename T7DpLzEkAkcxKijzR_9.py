
def cars_needed(n):
    capacity = 5
​
    # Full cars is equal to amount of passengers / capacity of cars, rounded
    # to full numbers
    cars_full = n // capacity
​
    # If there are any leftover passengers that couldn't fit in full cars,
    # return the amount of full cars plus one extra car
    if n % capacity:
        return cars_full + 1
    else:
        return cars_full

