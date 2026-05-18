from product import Product
import inventory_manager as inventory_manager_nbs


def add_product_nbs():
    try:
        product_id_nbs = input("Enter Product ID: ").strip()
        name_nbs = input("Enter Product Name: ").strip()
        price_nbs = float(input("Enter Price: ").strip())
        quantity_nbs = int(input("Enter Quantity: ").strip())

        if not product_id_nbs or not name_nbs:
            raise ValueError("Product ID and name cannot be empty.")

        product_nbs = Product(product_id_nbs, name_nbs, price_nbs, quantity_nbs)
        inventory_manager_nbs.save_product_nbs(product_nbs)
        print("Product added successfully")
    except ValueError:
        print("Invalid input")
    except Exception as e_nbs:
        print("Error:", e_nbs)


def view_products_nbs():
    inventory_manager_nbs.view_products_nbs()


def search_product_nbs():
    product_id_nbs = input("Enter Product ID: ").strip()
    if not product_id_nbs:
        print("Invalid input")
        return
    product_nbs = inventory_manager_nbs.find_product_by_id_nbs(product_id_nbs)
    if product_nbs:
        print("Product Found:")
        print(product_nbs)
    else:
        print("Product not found")


def update_quantity_nbs():
    product_id_nbs = input("Enter Product ID: ").strip()
    if not product_id_nbs:
        print("Invalid input")
        return
    try:
        quantity_nbs = int(input("Enter new Quantity: ").strip())
        if quantity_nbs < 0:
            raise ValueError("Quantity cannot be negative")
        updated_nbs = inventory_manager_nbs.update_product_quantity_nbs(product_id_nbs, quantity_nbs)
        if updated_nbs:
            print("Quantity updated successfully")
        else:
            print("Product not found")
    except ValueError:
        print("Invalid quantity")


def main_nbs():
    while True:
        print("\nINVENTORY MANAGEMENT SYSTEM")
        print("1 Add Product")
        print("2 View Products")
        print("3 Search Product")
        print("4 Update Quantity")
        print("5 Exit")

        choice_nbs = input("Enter choice: ").strip()
        if choice_nbs == "1":
            add_product_nbs()
        elif choice_nbs == "2":
            view_products_nbs()
        elif choice_nbs == "3":
            search_product_nbs()
        elif choice_nbs == "4":
            update_quantity_nbs()
        elif choice_nbs == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main_nbs()

#Nicole B. Sambile