
# Exide Inverter Selector
"""This is a program which helps you to select the right inverter and battery for your home and office."""
# Getting user details
def get_user_details():
    """This function gets the user details."""
    print("Welcome to Exide Inverter Selector")
    name = input("Enter your name: \n")
    print("Hello", name, "!")
    mob_no = input("Enter your mobile number: \n")
    print("Thank you for providing your details", name, "!")   
    return name, mob_no

def get_inverter_details():
    """This function gets the inverter details."""
    print("Please provide the following details to know the suitable inverter for your home and office:3\n")
    choice = input("Do you know your load requirement in watt? (Y/N)")
    if choice == 'Y' or 'y':
        load = int(input("Enter your load requirement in watt: \n"))
    elif choice == 'N' or 'n':
        print("Please provide the details to know your load in wattage:\n")
        no_fans = int(input("Enter the number of fans you want to run: (Upto 75W)\n"))
        no_tubelights = int(input("Enter the number of tubelights you want to run: (Upto 40W)\n"))
        no_cfl = int(input("Enter the number of CFL you want to run: (Upto 25W)\n"))
        no_tv = int(input("Enter the number of TV you want to run: (Upto 32in)\n"))
        no_tv2 = int(input("Enter the number of TV you want to run: (Upto 65in)\n"))
    else:
        print("Please enter a valid input")
    

def get_battery_details():
    """This function gets the battery details."""
    print("Please provide the following details to know the suitable battery for your home and office:\n")
    choice = input("Do you know your backup requirement in hours? (Y/N)")
    if choice == 'Y' or 'y':
        backup = int(input("Enter your backup requirement in hours: \n"))
    else:
        print("Please enter a valid input")
                      
def get_user_choice():
    choice = input("Do you want to search for \n1] Inverter \n2]Inverter battery?\n")
    if choice == '1':
        get_inverter_details()
    elif choice == '2':
        get_battery_details()
    else:
        print("Please enter a valid input")
get_user_choice()



