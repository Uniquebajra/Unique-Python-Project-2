
def main_header():
    print("______________________________________________________________________________________________")
    print("                            Greetings from the ABC laptop shop.                               ")
    print("                       Let's get started with the transaction process                         ")
    print("______________________________________________________________________________________________\n\n")


def inventory(inventory_dict):
    print("\t\t\t\t\t\tHello!\n\t\t\t\t\tWelcome to Our Store\n\t\t\t\tThe following laptops are available")
    headers = ["Item No.", "Name", "Brand", "CPU", "GPU", "Price", "Stock"]
    print("---"*39)
    print('| {:^10} | {:^25} | {:^10} | {:^15} | {:^15} | {:^10} | {:^10} |'.format(*headers))
    print("---"*39)

    for key in inventory_dict.keys():
        row = [key, *inventory_dict[key].values()]
        print('| {:^10} | {:^25} | {:^10} | {:^15} | {:^15} | {:^10} | {:^10} |'.format(*row))
    
    print("---"*39)


def laptop_table():
    def display_laptops():
        # In this case, "r" stands for the read function.
        # file = open("C:\Users\kriti\OneDrive\Desktop\Unique Python Project\Document.txt", "r")
        file_path = r"C:\Users\kriti\OneDrive\Desktop\Unique Python Project\Document.txt"
        with open(file_path, "r") as file:
            # Do something with the file object
            laptop_ID = 1  # For the item number
            for line in file:
                # Python has a built-in function called replace().
                print("\t", laptop_ID,  "\t|"+line.replace(",", "     |   "))
                laptop_ID = laptop_ID+1
            print("---------------------------------------------------------------------------------------------------------------------------------")
        file.close()
    display_laptops()     