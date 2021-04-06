
def items_purchase(store, wallet):
  return "Nothing" if all(int(i[1:].replace(",", "")) > int(wallet[1:]) for i in store.values()) else \
    sorted(key for key, value in store.items() if int(value[1:].replace(",", "")) <= int(wallet[1:]))

