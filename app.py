def show_options_of_the_main_menu():
    print("1. Register restaurant")
    print("2. List restaurant")
    print("3. Restaurant status")
    print("4. Exit")

def choosen_option():
    try:
        choose_option = int(input("\nChoose an option: "))
        match choose_option:
            case 1:
                print("Register restaurant!")
            case 2:
                print("List the registered restaurants!")
            case 3:
                print("Shows the status of the restaurant!")
            case 4:
                print("End the program!")
            case _:
                print("Invalid option!")
    except:
        print("Invalid option. Enter a number!")

def main_menu():
    show_options_of_the_main_menu()
    choosen_option()

if __name__ == "__main__":
    main_menu()