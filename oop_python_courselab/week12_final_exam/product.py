class Product:
    def __init__(self_nbs, product_id_nbs, name_nbs, price_nbs, quantity_nbs):
        self_nbs.__product_id_nbs = product_id_nbs.strip()
        self_nbs.__name_nbs = name_nbs.strip()
        self_nbs.__price_nbs = price_nbs
        self_nbs.__quantity_nbs = quantity_nbs

    def get_product_info(self_nbs):
        return f"{self_nbs.__product_id_nbs},{self_nbs.__name_nbs},{self_nbs.__price_nbs},{self_nbs.__quantity_nbs}"

    def get_id_nbs(self_nbs):
        return self_nbs.__product_id_nbs

    def update_quantity_nbs(self_nbs, quantity_nbs):
        self_nbs.__quantity_nbs = quantity_nbs

    def __str__(self_nbs):
        return f"{self_nbs.__product_id_nbs} | {self_nbs.__name_nbs} | {self_nbs.__price_nbs} | {self_nbs.__quantity_nbs}"

#Nicole B. Sambile