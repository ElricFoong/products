products = []
print("Type q for exit")
while True:
    name = input("Products name ")
    if name == "q":
        break
    price = input("Products price ")
    products.append([name, price])

print(products)
