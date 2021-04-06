
def has_valid_price(product):
  return (
    bool(product)
    and "price" in product
    and isinstance(product['price'], (int, float))
    and product["price"] >= 0
  )

