from datetime import date
import random
import invoice


def get_single_order(inventory_dict, order_dict):
    ##--Asks the user to input the ID od the Laptop to be purchased--##
    have_laptop_id = False
    while have_laptop_id == False: 
        try:
            laptop_id = int(input("Please specify a specific ID of the Laptop: "))
            if laptop_id not in inventory_dict.keys():
                print("*****Please enter a valid laptop ID*****")
            else:
                have_laptop_id = True
        except:
            print("\t\t*****Please enter a valid command*****")


    ##--Asks the user to input the number of laptops to be purchased--##
    quantity_entered = False
    while quantity_entered == False:
        try:
            laptop_quantity = int(input("Enter the number of Laptop you want to order: "))
            if laptop_quantity <= 0:
                print("Please enter a valid quantity")        
            else:
                quantity_entered = True   
        except:
            print("\n*****Please enter a valid number*****\n")
    
    if laptop_id in order_dict:
        order_dict[laptop_id] = {
            **inventory_dict[laptop_id],
            "stock": order_dict[laptop_id]["stock"] + laptop_quantity,
        }
    else:
        order_dict[laptop_id] = {
            **inventory_dict[laptop_id],
            "stock": laptop_quantity,
        }

    # increasing stock in inventory when new items are purchased
    inventory_dict[laptop_id]["stock"] += laptop_quantity
    return order_dict

def purchase_order(inventory_dict):
    random_num = str(random.randint(10000, 99999))
    current_date = str(date.today())
    invoice_no = current_date + '-' + random_num

    distributor_name = input("Please enter the name of the distributor: ")
    phone_number = "9838493489"
    phonenumber_needed = True
    while phonenumber_needed == True:
        try:
            phone_number = input("Enter the phone number of the customer: ")
            length = len(phone_number)
            if length == 10 and phone_number[0] == "9" and phone_number[1] == "8" and phone_number.isdigit:
                phonenumber_needed = False
            else :
                print("**Please enter valid 10 digit phone number starting with 98***")
        except:
            print("**Please enter valid 10 digit phone number starting with 98***")

    order_details_dict = {
        "invoice_no": invoice_no,
        "order_date": current_date,
        "distributor_name": distributor_name,
        "phone_number": phone_number,
    }

    
    get_new_order = True
    order_dict = {}
    ####--counting the number of laptops that  are available in the store --####
    while get_new_order == True:
        order_dict = get_single_order(inventory_dict, order_dict)
        sell_again = input("If you want to purchase again, press 'Y' for YES and any other keys for NO: ").lower()
        if sell_again != "y":
            get_new_order = False    
    
    total_amount = 0
    for value in order_dict.values():
        price = value['price']
        quantity = value['stock']
        total_amount += price * quantity
    
    VAT = 0.13
    total_vat = total_amount * VAT
    
    total_dict = {
        "net_amount": total_amount,
        "VAT": total_vat,
        "gross_amount_with_VAT": total_amount + total_vat,
    } 

    invoice.create_purchase_invoice(order_details_dict, order_dict, total_dict)