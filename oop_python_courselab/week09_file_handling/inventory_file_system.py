product_nbs = input("Enter product name: ")
price_nbs = input("Enter price: ")

with open("inventory.txt", "a") as file:
    file.write(product_nbs + "," + price_nbs + "\n")

print("Product saved successfully")

#Nicole Sambile