import os   # Operating system                                    #  refactor 重构

#  读取资料


def read_file(filename):
    products = []
    with open(filename, "r", encoding="utf-8")as f:
        for line in f:
            if "商品,价格" in line:
                continue
            name, price = line.strip().split(",")
            products.append([name, price])
    return products

#   商品输入


def user_input(products):
    while True:
        name = input("请输入商品名称 ")
        if name == "q":
            break
        price = int(input("请输入商品价格 "))
        products.append([name, price])
    print(products)
    return products

#   印出商品和价格


def print_products(products):
    for p in products:
        print(p[0], "的价格是, ", p[1])

#     写入资料


def write_file(filename, products):
    with open(filename, "w", encoding="utf-8")as f:
        f.write("商品,价格\n")
        for p in products:
            f.write(p[0] + "," + str(p[1]) + "\n")


def main():
    filename = "products.csv"
    products = []               # 如果 products = [] 放在 第40行， 就会 覆盖overwrite资料。
    if os.path.isfile(filename):
        print("找到档案")
        # 读取local variable 的 filename,然后储存在 products.
        products = read_file(filename)
    else:
        print("找不到档案")
        #  如果 products = [] 放在 46行， 就不会 覆盖overwrite资料。
    # 从第43行的product 投进 user_input(products)里，执行后再存入products 里
    products = user_input(products)
    print_products(products)  # 47行的 products 投进 print_products(products)里
    write_file("products.csv", products)  # 写入档案（文件名称， 以上所有执行了的资料）


main()
