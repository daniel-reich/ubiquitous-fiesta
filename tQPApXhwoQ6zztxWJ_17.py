
import re
​
def get_prices(lst: list) -> list:
    """Return a list of prices in float format."""
    return [float(item) for item in re.findall("(\d+\.\d+)", "".join(lst))]

