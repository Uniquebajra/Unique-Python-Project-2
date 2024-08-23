def update_inventory(inventory_dict):
    inventory_file = open("Document.txt", "w")  #re-write the Original Document.txt file
    for value in inventory_dict.values():
        inventory_file.write(",".join([
            value['name'],
            value['brand'],
            value['processor'],
            value['gpu'],
            str(value['price']),
            str(value['stock']),
        ])+"\n")
    inventory_file.close()