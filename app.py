import os

def show_options_of_the_main_menu():
    print("1. Register restaurant")
    print("2. List restaurant")
    print("3. Restaurant status")
    print("4. Exit")

def shows_subtitles(text):
    os.system("cls")
    line = "=" * (len(text))
    print(line)
    print(text)
    print(line, "\n")

def return_to_the_main_menu():
    input("\nPress a key + the ENTER key to return to the main menu: ")
    main_menu()

def invalid_option():
    print("Invalid option. Try again!")
    return_to_the_main_menu

def finish_app():
    shows_subtitles("Program finished with successfully!")

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
                finish_app()
            case _:
                invalid_option()
    except:
        print("Invalid option. Enter a number!")

def main_menu():
    show_options_of_the_main_menu()
    choosen_option()

if __name__ == "__main__":
    main_menu()