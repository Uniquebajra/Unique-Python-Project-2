
def invoice_title():
    invoice_title = "************************************************************************************************\n"
    invoice_title += "************************************XYZ Laptop Store********************************************\n"
    invoice_title += "*                                   Kathmandu, Nepal                                           *\n"
    invoice_title += "*                                  Contact - 9864238612                                        *\n"
    invoice_title += "************************************************************************************************\n"
    return invoice_title

def create_sale_invoice(order_details_dict, order_dict, total_dict):
    file_name = "Sale Invoices/Sale Invoice {} to {}.txt".format(order_details_dict["invoice_no"], order_details_dict["customer_name"])
    invoice_file = open(file_name, "w")
    invoice_file.write(invoice_title())
    invoice_file.write("\n")

    order_details = [
        "\t {:<25} {:>40}\n".format("Invoice No", order_details_dict["invoice_no"]),
        "\t {:<25} {:>40}\n".format("Ordered Date", order_details_dict["order_date"]),
        "\t {:<25} {:>40}\n".format("Customer Name", order_details_dict["customer_name"]),
        "\t {:<25} {:>40}\n".format("Phone Number", order_details_dict["phone_number"]),
        "\n"
    ]
    invoice_file.writelines(order_details)

    dashed_line_border = "---"*32 + "\n"
    headers = ["Name", "Brand", "Unit Price", "Quantity", "Total"]
    invoice_file.write(dashed_line_border)
    invoice_file.write('| {:^25} | {:^15} | {:^15} | {:^15} | {:^10} |\n'.format(*headers))
    invoice_file.write(dashed_line_border)

    for value in order_dict.values():
        row = [value["name"], value["brand"], value["price"], value["stock"], value["price"] * value["stock"]]
        invoice_file.write('| {:^25} | {:^15} | {:^15} | {:^15} | {:^10} |\n'.format(*row))
    invoice_file.write(dashed_line_border)
    invoice_file.write("\n")

    
    order_details = [
        "\t {:<25} {:>40}\n".format("Invoice No", order_details_dict["invoice_no"]),
        "\t {:<25} {:>40}\n".format("Ordered Date", order_details_dict["order_date"]),
        "\t {:<25} {:>40}\n".format("Customer Name", order_details_dict["customer_name"]),
        "\t {:<25} {:>40}\n".format("Phone Number", order_details_dict["phone_number"]),
        "\n"
    ]
    invoice_file.write("\t {:<25} {:>40}\n".format("Total amount", total_dict["total_amount"]))
    if total_dict["shipping_cost"] > 0:
        invoice_file.write("\t {:<25} {:>40}\n".format("Shipping cost", total_dict["shipping_cost"]))
        invoice_file.write("\t {:<25} {:>40}\n".format("Total with shipping", total_dict["total_amount_with_shipping"]))
    invoice_file.write("\n")
    invoice_file.write(dashed_line_border)
    invoice_file.close()

    print_invoice(file_name)


def print_invoice(file_name):
    invoice_file = open(file_name, "r")
    print(invoice_file.read())
    invoice_file.close()


def create_purchase_invoice(order_details_dict, order_dict, total_dict):
    file_name = "Purchase Invoices/Purchase Invoice {} from {}.txt".format(order_details_dict["invoice_no"], order_details_dict["distributor_name"])
    invoice_file = open(file_name, "w")
    invoice_file.write(invoice_title())
    invoice_file.write("\n")

    order_details = [
        "\t {:<25} {:>40}\n".format("Invoice No", order_details_dict["invoice_no"]),
        "\t {:<25} {:>40}\n".format("Ordered Date", order_details_dict["order_date"]),
        "\t {:<25} {:>40}\n".format("Distributor Name", order_details_dict["distributor_name"]),
        "\t {:<25} {:>40}\n".format("Phone Number", order_details_dict["phone_number"]),
        "\n"
    ]
    invoice_file.writelines(order_details)

    dashed_line_border = "---"*32 + "\n"
    headers = ["Name", "Brand", "Unit Price", "Quantity", "Total"]
    invoice_file.write(dashed_line_border)
    invoice_file.write('| {:^25} | {:^15} | {:^15} | {:^15} | {:^10} |\n'.format(*headers))
    invoice_file.write(dashed_line_border)

    for value in order_dict.values():
        row = [value["name"], value["brand"], value["price"], value["stock"], value["price"] * value["stock"]]
        invoice_file.write('| {:^25} | {:^15} | {:^15} | {:^15} | {:^10} |\n'.format(*row))
    invoice_file.write(dashed_line_border)
    invoice_file.write("\n")

    invoice_file.write("\t {:<25} {:>40}\n".format("Net amount", total_dict["net_amount"]))
    invoice_file.write("\t {:<25} {:>40}\n".format("VAT", total_dict["VAT"]))
    invoice_file.write("\t {:<25} {:>40}\n".format("Total with VAT", total_dict["gross_amount_with_VAT"]))
        
    invoice_file.write("\n")
    invoice_file.write(dashed_line_border)
    invoice_file.close()

    print_invoice(file_name)

    
if __name__ == "__main__":
    order_details_dict = {'invoice_no': '2023-05-05-28244', 'order_date': "2023-02-23", 'customer_name': 'nIk', 'phone_number': '9898989898'}
    order_dict = {3: {'name': '  Alienware m15', 'brand': 'Alienware', 'processor': 'i5 9th Gen', 'gpu': 'GTX 3070', 'price': 1978, 'stock': 2}}

    total_dict = {
        "total_amount": 10000,
        "shipping_cost": 200,
        "total_amount_with_shipping": 1200,
    }
    create_sale_invoice(order_details_dict, order_dict, total_dict)


    # create purchase invoice
    order_details_dict = {'invoice_no': '2023-05-05-28244', 'order_date': "2023-02-23", 'distributor_name': 'nIk', 'phone_number': '9898989898'}
    order_dict = {3: {'name': '  Alienware m15', 'brand': 'Alienware', 'processor': 'i5 9th Gen', 'gpu': 'GTX 3070', 'price': 1978, 'stock': 2}}

    total_dict = {
        "net_amount": 10000,
        "VAT": 200,
        "gross_amount_with_VAT": 1200,
    }
    create_purchase_invoice(order_details_dict, order_dict, total_dict)