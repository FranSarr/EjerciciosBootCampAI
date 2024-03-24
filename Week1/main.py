import os

def chef1_script():
    os.system("python Chef_GTP_AnisHM.py")

def chef2_script():
    os.system("python ChefGPT_Arkano_eth.py")

def chef3_script():
    os.system("python ChefGPT_F0x.py")

def chef4_script():
    os.system("python ChefGPT_NadaJ.py")

def chef5_script():
    os.system("python ChefGPT_NicolasV.py")

def chef6_script():
    os.system("python ChefGPT_teacherjavier.py")

def display_menu():
    print("Select a chef:")
    print("1. Chef 1 experienced female french chef specialized in cuisine bretonne")
    print("2. Chef 2 experienced Argentinian chef specialized in meats, barbeque and dulce de leche specialities")
    print("3. Chef 3 experienced Hungarian chef specialized in East European food.")
    print("4. Chef 4 experienced israeli chef specialized in Kosher dishes")
    print("5. Chef 5 experienced french chef specialized in food from the Provence et Midi.")
    print("6. Chef 6 an amateur spanish cook that loves traditional Mediterranean recipes")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            chef1_script()
        elif choice == '2':
            chef2_script()
        elif choice == '3':
            chef3_script()
        elif choice == '4':
            chef4_script()
        elif choice == '5':
            chef5_script()
        elif choice == '6':
            chef6_script()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 6.")

if __name__ == "__main__":
    main()