
def license_plate(plate, n):
    return license_plate_rec(plate, n)[::-1].upper()
​
def license_plate_rec(plate, n):
    plate = plate[::-1].replace("-", "")
    return plate if len(plate) <= n else plate[:n] + "-" + license_plate_rec(plate[n:][::-1], n)

