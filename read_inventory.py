def read_inventory():
    file = open("Document.txt", "r")
    laptop_dict = {}

    laptop_id = 1
    for line in file:
        line = line.replace("\n", "")
        [name, brand, processor, gpu, price, stock] = line.split(",")
        laptop_dict[laptop_id] = {
            "name": name,
            "brand": brand,
            "processor": processor,
            "gpu": gpu,
            "price": int(price),
            "stock": int(stock),
        }
        laptop_id += 1
    file.close()
    return laptop_dict


if __name__ == "__main__":
    laptop_dict = read_inventory()
    print(laptop_dict)