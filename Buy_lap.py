from datetime import date
import random

def Order():
    
    def Laptop_dictonary():  #Creating laptop dictonary
        file = open("Document.txt", "r")
        laptop_dict = {}

        laptop_ID = 1
        for line in file:
            line = line.replace("\n", "")
            laptop_dict.update({laptop_ID: line.split(",")})
            laptop_ID = laptop_ID + 1
        file.close()
        

        return laptop_dict

    

    def table(laptop_dict):  #it counts the list of the dictonary and stores list of numebers inside the list
        number_list = []
        for i in range(len(laptop_dict)):
            number_list.append(i+1)
        
        return number_list

   
    def validating_order(laptop_dict, number_list):    #it is the looping process of the system. The loop runs continuously without any error even if the user input the invalid command

        distributor_name = input("Please enter the name of the Distributor Company: ")
        
        random_num = str(random.randint(10000, 99999))
        current_date = str(date.today())

        invoice_no = current_date + '-' + random_num

        

        phonenumber_needed = True
        while phonenumber_needed == True:
            try:
                phone_number = input("Enter the phone number: ")
                length = len(phone_number)
                if length == 10 and phone_number[0] == "9" and phone_number[1] == "8" :
                    phonenumber_needed = False
                else :
                    print("*****Invalid Phone Number*****")
            except:
                print("*****Invalid Phone Number*****")





        file = open("%s %s.txt" % ("Bought from ", distributor_name,), "w")  #it makes the file for the customers with the name of the customers
        file.write("\n************************************************************************************************"
                   "\n************************************%s********************************************"
                   "\n                                    Kathmandu, Nepal                                            "
                   "\n                                   Contact - 9864238612                                         "
                   "\n**********************************************************************************************\n" % (distributor_name))
        file.write(3*"\n") 


        file.write("%s %s" % ("invoice No: ", invoice_no))
        
        file.write("\n")
        file.write("%s" % ("Ordered Date: "))
        file.write(str(date.today()))
        file.write("\n")


        file.write("\n\n%s\n" % ("\t\tName: ABC Laptop Shop"))               #writes inside the file of customer
        file.write("%s %s\n" % ("\t\tPhone Number: ", phone_number)) 
        ############################################################################
        file.write("\n********************************************************************************************\n")

        file.write("\t\tLaptop Name\t\tBrand\t\tquantity\tPrice")
        file.write("\n********************************************************************************************")

        
        
        loop = True
        price_of_laptop = 0
        total_Qunatity = 0
        
        ####--counting the number of laptops that  are available in the store --####
        while loop == True:


            ##--Asks the user to input the ID od the Laptop to be sold--##
            have_laptop_id = False
            while have_laptop_id == False: 
                try:
                    laptop_id_input = int(input("Enter the ID of the laptop You want to place an order on: "))
                    if laptop_id_input <= 0 or laptop_id_input > len(laptop_dict):
                        print("*****Please enter a valid ID*****")
                    else:
                        have_laptop_id = True
                except:
                    print("\t\t*****Please enter a valid command*****")


            ##--Asks the user to input the number of laptops to be sold--##
            quantity = False
            while quantity == False:
                try:
                    laptop_quantity = int(input("Enter the number of Laptop you want to order: "))
                    if laptop_quantity <= 0 or laptop_quantity > int(laptop_dict[laptop_id_input][5]):
                        print("*****Please enter a valid number*****")
                       
                        
                            
                    else:
                        quantity = True
                        
                    
                except:
                    print("\n*****Please enter a valid command*****\n")
                    
                    
         ####--     Asking the user repeatedly if they want to sell the laptop      --####
            
            for i in number_list:

                if laptop_id_input == number_list[i-1]: #It checks if the laptop id inputed is present in the list 
                    
                    
                    price_of_laptop = price_of_laptop + int(laptop_dict[i][4])
                    laptop_dict[i][5] = int(
                        laptop_dict[i][5]) + laptop_quantity
                    total_Qunatity =total_Qunatity+laptop_quantity
                    
                    print("Thank you. I hope you will  enjoy!")
                    
                    ###############################################################################
                    file.write("\n\t\t%s\t%s\t  %s\t\t%s" % (laptop_dict[i][0], laptop_dict[i][1], int(laptop_quantity), int(laptop_dict[i][4])))            








                    shipping_cost = 200
                    



                   

                    sell_again = input("If you want to Order again, press 'Y' for YES and any other keys for NO: ").lower()
                    if sell_again == "y":
                        loop = True    
                    else: 
                        

                        shipping_needed = input("do you want the laptop to be delivered?press 'Y' for YES and any other keys for NO: ")
                        if shipping_needed == "y":
                            
                            total_Qunatity_shipping = (laptop_quantity*price_of_laptop) + shipping_cost
                            loop = False
                        else:
                            total_Qunatity_shipping = laptop_quantity*price_of_laptop
                            shipping_cost = 0
                            loop = False

                        
                    
                    
        file.write("\n********************************************************************************************\n")        
        file.write("%s %d\t\t%d\n\n" % ("\t\tTotal\t\t\t\t\t ", total_Qunatity, laptop_quantity*price_of_laptop))    
        
        VAT_amount = (13 /100 ) *  (laptop_quantity * price_of_laptop)  
        Total_VAT_Shipping = total_Qunatity_shipping + VAT_amount

        
                  
        file.write("%s %d\n" % ("\t\tTotal number of laptops purchased: ", total_Qunatity))   
        file.write("%s %5.1f %s\n" % ("\t\tYour total amount is :", laptop_quantity*price_of_laptop, "dollars"))

        file.write("%s %s\n" % ("\t\tShipping cost: ", shipping_cost))
        file.write("%s %s\n" % ("\t\tVAT Amount: ", VAT_amount))

        file.write("%s %s" % ("\t\tTotal cost with shipping cost and VAT: ", Total_VAT_Shipping))

        
    
        file.write("\n************************************************************************************************\n\n\n")
        file.close()
 

        return distributor_name
    


    
        





    def Update_lap_table(laptop_dict):
        file_again = open("Document.txt", "w")  #re-write the Original Document.txt file
        for values in laptop_dict.values():
            file_again.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4]+","+str(values[5])))
            file_again.write("\n")
        file_again.close()
            

        #################----       Invoice     ---######################

    def Invoice(customer_name):
        file = open("%s %s.txt" % ("Rented by ", customer_name), "r")
        for line in file:
            print(line)
        file.close()
        
    Dictonary_laptop = Laptop_dictonary()  
    
    Add_dict = table(Dictonary_laptop) 
    
    looping = validating_order(Dictonary_laptop, Add_dict) 
    
    Update_table = Update_lap_table(Dictonary_laptop)
    
    Invoice_Bill = Invoice(looping)
    
