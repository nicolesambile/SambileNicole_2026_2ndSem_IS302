import os

PRODUCTS_FILE_NBS = os.path.join(os.path.dirname(__file__), "products.txt")


def save_product_nbs(product_nbs):
    try:
        with open(PRODUCTS_FILE_NBS, "a", encoding_nbs="utf-8") as file_nbs:
            file_nbs.write(product_nbs.get_product_info() + "\n")
    except Exception as e_nbs:
        print("Error saving product:", e_nbs)


def view_products_nbs():
    try:
        with open(PRODUCTS_FILE_NBS, "r", encoding_nbs="utf-8") as file_nbs:
            lines_nbs = [line.strip() for line in file_nbs if line.strip()]
            if not lines_nbs:
                print("No products found.")
                return
            print("Product ID | Name | Price | Quantity")
            for line_nbs in lines_nbs:
                product_nbs = parse_line_to_product_nbs(line_nbs)
                print(product_nbs)
    except FileNotFoundError:
        print("No products found.")


def find_product_by_id_nbs(product_id_nbs):
    try:
        with open(PRODUCTS_FILE_NBS, "r", encoding_nbs="utf-8") as file_nbs:
            for line_nbs in file_nbs:
                if not line_nbs.strip():
                    continue
                product_nbs = parse_line_to_product_nbs(line_nbs.strip())
                if product_nbs.get_id_nbs() == product_id_nbs:
                    return product_nbs
    except FileNotFoundError:
        return None
    return None


def update_product_quantity_nbs(product_id_nbs, quantity_nbs):
    try:
        updated_nbs = False
        products_nbs = []
        with open(PRODUCTS_FILE_NBS, "r", encoding_nbs="utf-8") as file_nbs:
            for line_nbs in file_nbs:
                if not line_nbs.strip():
                    continue
                product_nbs = parse_line_to_product_nbs(line_nbs.strip())
                if product_nbs.get_id_nbs() == product_id_nbs:
                    product_nbs.update_quantity_nbs(quantity_nbs)
                    updated_nbs = True
                products_nbs.append(product_nbs)

        if not updated_nbs:
            return False

        with open(PRODUCTS_FILE_NBS, "w", encoding_nbs="utf-8") as file_nbs:
            for product_nbs in products_nbs:
                file_nbs.write(product_nbs.get_product_info() + "\n")
        return True
    except FileNotFoundError:
        return False
    except Exception as e_nbs:
        print("Error updating product quantity:", e_nbs)
        return False


def parse_line_to_product_nbs(line_nbs):
    parts_nbs = line_nbs.split(",")
    if len(parts_nbs) != 4:
        raise ValueError("Invalid product record format")
    product_id_nbs = parts_nbs[0].strip()
    name_nbs = parts_nbs[1].strip()
    price_nbs = float(parts_nbs[2].strip())
    quantity_nbs = int(parts_nbs[3].strip())
    from product import Product
    return Product(product_id_nbs, name_nbs, price_nbs, quantity_nbs)

#Nicole B. Sambile