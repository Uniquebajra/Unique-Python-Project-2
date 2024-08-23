import display
import purchase_order
import sale_order
import read_inventory
import update_inventory

def main():
    display.main_header()
    loop = True
    while loop == True:
        try:
            while loop == True:
                print("Press 1 to display the laptops")
                print("Press 2 to start the selling process")
                print("Press 3 to start the buying process")
                print("Press 4 to exit\n")
                user_input = int(input("Enter the option: "))
                inventory_dict = read_inventory.read_inventory()
                if user_input == 1:
                    display.inventory(inventory_dict)
                elif user_input == 2:
                    print("\t\tgetting started with the selling process.")
                    display.inventory(inventory_dict)
                    sale_order.sale_order(inventory_dict)
                    update_inventory.update_inventory(inventory_dict)
                elif user_input == 3:
                    print("\t\tgetting started with the purchasing process.")
                    display.inventory(inventory_dict)
                    purchase_order.purchase_order(inventory_dict)
                    update_inventory.update_inventory(inventory_dict)
                elif user_input == 4:
                    print("\t\tyou exited the system")
                    loop = False
                else:
                    print("***Please enter a valid option***")
        except:
            print("***Error: please enter a valid command***")

main()
