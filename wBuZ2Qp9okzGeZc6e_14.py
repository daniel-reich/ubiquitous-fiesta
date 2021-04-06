
def first_place(road):
  print(road)
  try:
    count = 1
    while road[-count] == "=":
      count += 1
    print(count)
    print(road[-count])
    return road[-count]
  except:
    print(None)
    return None

