
# Return an empty string if the house is a valid size
def valid_house_size_check(hh, hw, hd, rh):
  # House height check
  if (hh + rh) > 20:
    return "No permission."
  
  # Width check to see if door & windows can fit
  if (hw < 15) or (hd < 11):
    return "House too small."
  
  # House size check: Can it fit in the garden with 3 ft of space around it?
  if ((hw + 6) > 50) or ((hd + 6) > 50):
    return "House too big."
  
  return ""
​
def we_have_house(hh, hw, hd, rh):
  invalid_house_msg = valid_house_size_check(hh, hw, hd, rh)
  
  if invalid_house_msg:
    return invalid_house_msg
​
  # Area of all windows + area of the door that's in the yellow wall section
  area_of_objects_in_yellow_section = (8 * (3 * 4)) + (3 * 5)
  area_of_yellow_section = (2 * (hh - 2) * (hw + hd)) + (hw * rh)
  yellow_paint = area_of_yellow_section - area_of_objects_in_yellow_section
  
  # Bottom portion of the door in the gray wall section
  area_of_objects_in_gray_section = 3 * 2
  area_of_gray_section = 2 * (2 * (hw + hd))
  gray_paint = area_of_gray_section - area_of_objects_in_gray_section
  
  return "Yellow: {}, Gray: {}".format(yellow_paint, gray_paint)

