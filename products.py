products = []
print("Please type q for exit ")

while True:
    name = input("Products name ")
    if name == "q":
        break
    price = input("Products price ")
    products.append([name, price])

print(products)


for product in products:
    print(product[0], "price is ", product[1])

with open("products.csv", "w") as f:
    for p in products:
        f.write(p[0] + "," + p[1] + "\n")
