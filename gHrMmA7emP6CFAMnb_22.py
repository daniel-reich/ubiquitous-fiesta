
def is_apocalyptic(number):
  return "Single" if str(2 ** number).count("666") == 1 \
    else "Double" if str(2 ** number).count("666") == 2 \
    else "Triple" if str(2 ** number).count("666") == 3 \
    else "Safe"

