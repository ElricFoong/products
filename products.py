products = []
#  读取档案
with open("products.csv", "r", encoding="utf-8")as f:
    for lines in f:
        if "商品, 价格" in lines:
            continue
        name, price = lines.strip().split(",")
        products.append([name, price])
print(products)
#  输入商品名称与价格
while True:
    name = input("请输入商品名称 ")
    if name == "q":
        break
    price = input("请输入商品价格 ")
    products.append([name, price])
print(products)
# 写入档案
with open("products.csv", "w", encoding="utf-8")as f:
    f.write("商品, 价格 \n")
    for p in products:
        f.write(p[0] + "," + p[1] + "\n")
