
def total_sales(sales_table, product):
    return {values[0]: sum(values[1:]) for values in zip(*sales_table)}.get(product, 'Product not found')

