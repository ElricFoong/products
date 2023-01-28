products = []
print("Please type q for exit ")

while True:
    name = input("Products name ")
    if name == "q":
        break
    price = int(input("Products price "))
    products.append([name, price])

print(products)


for product in products:
    print(product[0], "价格是 ", product[1])

with open("products.csv", "w", encoding="utf-8") as f:
    f.write("商品，价格 \n")
    for p in products:
        f.write(p[0] + "," + str(p[1]) + "\n")
