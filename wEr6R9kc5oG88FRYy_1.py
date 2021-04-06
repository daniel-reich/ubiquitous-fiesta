
def get_frame(width, height, ch):
  if (width <= 2 or height <= 2):
    return "invalid";
  boundary  = [[ch * width]];
  contents  = [[ch + " " * (width-2) + ch]] * (height-2);
  return boundary + contents + boundary;

