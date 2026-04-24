class Product_nbs:
    def __init__(self_nbs, name_nbs, price_nbs, quantity_nbs):
        self_nbs.__name = name_nbs
        self_nbs.__price = price_nbs
        self_nbs.__quantity = quantity_nbs

    def get_product_info_nbs(self_nbs):
        print("Product:", self_nbs.__name)
        print("Price:", self_nbs.__price)
        print("Quantity:", self_nbs.__quantity)

    def update_quantity_nbs(self_nbs, new_quantity_nbs):
        if new_quantity_nbs >= 0:
            self_nbs.__quantity = new_quantity_nbs

    def update_price_nbs(self_nbs, new_price_nbs):
        if new_price_nbs > 0:
            self_nbs.__price = new_price_nbs

# Example usage
product_nbs = Product_nbs("Laptop", 45000, 10)
product_nbs.get_product_info_nbs()

#Nicole Sambile