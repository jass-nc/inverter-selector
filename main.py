# Exide Inverter Selector
"""This is a program which helps you to select the right inverter and battery for your home and office."""
# Getting user details
def get_user_details():
    """This function gets the user details."""
    print("Welcome to Exide Inverter Selector")
    name = input("Enter your name: \n")
    print("Hello", name, "!")
    mob_no = input("Enter your 10 digit mobile number: +91 ")
    if len(mob_no) == 10:
        pass
    else:
        print("Please enter a valid mobile number")
        mob_no = input("Enter your mobile number: +91 ")
    print("Thank you for providing your details", name, "!")   
    return name, mob_no

def get_inverter_details():
    """This function gets the inverter details."""
    print("Please provide the following details to know the suitable inverter for your home and office:3\n")
    choice = input("Do you know your load requirement in watt? (Y/N)\n")
    if choice == 'Y' or choice == 'y':
        print("Please enter the load requirement in watt: \n")
        load = int(input())
        print(f"Your load requirement is {load} watts")
        if load >= 0 and load <= 560:
            lkva_mod = ["1] Exide STAR12V700", "2] Exide STAR12V900", "3] Exide GQP12V700", "4] Exide GQP12V900", "5] Exide MAGIC12V800"]
            print("700VA to 900VA inverter is suitable for your home and office")
            print("In exide you can select inverters of model:")
            for i in lkva_mod:
                print(i)
        elif load>=561 and load<=900:
            lkva_mod = ["Exide STAR12V900","Exide STAR12V1125","Exide GQP12V1125", "Exide GQP12V900"]            
            print("900VA to 1125VA inverter is suitable for your home and office")
            print("In exide you can select inverters of model:")
            for i in lkva_mod:
                print(i)
        elif load>=901 and load<=1100:
            lkva_mod = ["1] Exide STAR12V1375","2] Exide GQP12V1375","3] Exide GQP12V1625", "4] Exide STAR12V1625", "5] Exide STAR24V1625"]
            print("1125VA to 1625VA inverter is suitable for your home and office")
            print("In exide you can select inverters of model:")
            for i in lkva_mod:
                print(i)
        elif load>=1101 and load<=1300:
            lkva_mod = ["1] Exide STAR12V1625","2] Exide GQP12V1625","3] Exide STAR24V1625", "4] Exide GQP24V1625"]
            print("1625VA inverter is suitable for your home and office")  
            print("In exide you can select inverters of model:")
            for i in lkva_mod:
                print(i)
        elif load>=1301:
            lkva_mod = ["1] Exide STAR24V2550","2] Exide GQP24V2550"]
            print("2550VA inverter is suitable for your home and office")
            print("In exide you can select inverters of model:")
            for i in lkva_mod:
                print(i)    
        elif load>2050:
            print("Call our executive to know the suitable inverter for your requirement")
            print("Contact us on +91 xxxxxxxxxx")                
  
    elif choice == 'N' or choice == 'n':
        print("\nPlease provide the details to know your load in wattage:\n")
        no_fans = int(input("Enter the number of fans you want to run: (Upto 75W)\n"))
        no_tubelights = int(input("Enter the number of tubelights you want to run: (Upto 40W)\n"))
        no_cfl = int(input("Enter the number of CFL you want to run: (Upto 25W)\n"))
        no_tv = int(input("Enter the number of TV you want to run: (Upto 32in)\n"))
        no_tv2 = int(input("Enter the number of TV you want to run: (Upto 65in)\n"))
        tot_load = (no_fans * 120) + (no_tubelights * 60) + (no_cfl * 45) + (no_tv * 160) + (no_tv2 * 200)
        print(f"Your load requirement is {tot_load} watts")
        if tot_load >= 0 and tot_load <= 560:
            lkva_mod = ["1] Exide STAR12V700", "2] Exide STAR12V900", "3] Exide GQP12V700", "4] Exide GQP12V900", "5] Exide MAGIC12V800"]
            print("700VA to 900VA inverter is suitable for your home and office")
            print("In exide you can select inverters of model:")
            for i in lkva_mod:
                print(i)
        elif tot_load>=561 and tot_load<=900:
            lkva_mod = ["Exide STAR12V900","Exide STAR12V1125","Exide GQP12V1125", "Exide GQP12V900"]            
            print("900VA to 1125VA inverter is suitable for your home and office")
            print("In exide you can select inverters of model:")
            for i in lkva_mod:
                print(i)
        elif tot_load>=901 and tot_load<=1100:
            lkva_mod = ["1] Exide STAR12V1375","2] Exide GQP12V1375","3] Exide GQP12V1625", "4] Exide STAR12V1625", "5] Exide STAR24V1625"]
            print("1125VA to 1625VA inverter is suitable for your home and office")
            print("In exide you can select inverters of model:")
            for i in lkva_mod:
                print(i)
        elif tot_load>=1101 and tot_load<=1300:
            lkva_mod = ["1] Exide STAR12V1625","2] Exide GQP12V1625","3] Exide STAR24V1625", "4] Exide GQP24V1625"]
            print("1625VA inverter is suitable for your home and office")  
            print("In exide you can select inverters of model:")
            for i in lkva_mod:
                print(i)
        elif tot_load>=1301:
            lkva_mod = ["1] Exide STAR24V2550","2] Exide GQP24V2550"]
            print("2550VA inverter is suitable for your home and office")
            print("In exide you can select inverters of model:")
            for i in lkva_mod:
                print(i)    
        elif tot_load>2050:
            print("Call our executive to know the suitable inverter for your requirement")
            print("Contact us on +91 xxxxxxxxxx")                
    else:
        print("Please enter a valid input")
    

def get_battery_details():
    """This function gets the battery details."""
    print("Please provide the following details to know the suitable battery for your home and office:\n")
    choice = int(input("Enter your backup requirement in hours: \n"))
    if choice >= 0 and choice <= 3:
        bat_mod = ["1] INVABRITE IBRFP4000", "2]INVABRITE IBRFP5000", "3] INVAHOMZ IHST1000", "4] INVAHOMZ IHST1500", "5] INVAMASTER IMST1000"]
        print("80AH to 150AH battery is suitable for your home and office\n")  
        print("In exide you can select batteries of model:\n")
        for i in bat_mod:
            print(i + "\n")
    elif choice > 3 and choice <= 6:
        bat_mod = ["1] INVABRITE IBRFP5000", "2] INVAHOMZ IHST1500", "3] INVAMASTER IMST1500", "4] INVAMASTER IMTT2000", "5] INVATUBULAR IT500"]
        print("150AH to 200AH battery is suitable for your home and office\n")
        print("In exide you can select batteries of model:\n")
        for i in bat_mod:
            print(i + "\n" )
    elif choice > 6 and choice <= 12:
        bat_mod = ["1] INVAHOMZ IHTT2000", "2] INVAMASTER IMTT2000", "3] INVATUBULAR IT750"]
        print("200AH battery is suitable for your home and office\n")
        print("In exide you can select batteries of model:\n")
        for i in bat_mod:
            print(i+"\n")
                      
def get_user_choice():
    get_user_details()
    choice = int(input("Do you want to search for \n1] Inverter \n2]Inverter battery?\n Enter your choice (1 or 2): "))
    if choice == 1:
        get_inverter_details()
    elif choice == 2:
        get_battery_details()
    else:
        print("Please enter a valid input")
get_user_choice()
