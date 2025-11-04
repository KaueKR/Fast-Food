import os

restaurant_lists = []

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

def registers_new_restaurant():
    shows_subtitles("Registration of new restaurants")
    restaurant_name = input("What is the name of the restaurant you want to register? ")
    restaurant_category = input(f"Enter the category of the restaurant {restaurant_name}: ")
    restaurant_data = {"name": restaurant_name, "category": restaurant_category, "state": False}
    restaurant_lists.append(restaurant_data)
    print(f"Restaurant {restaurant_name} successfully registered!")
    return_to_the_main_menu()

def list_of_registered_restaurants():
    shows_subtitles("List of registered restaurants: ")
    print(f"{"Restaurant Name".ljust(19)} {"Category".ljust(18)} {"State"}")
    for restaurant in restaurant_lists:
        restaurant_name = restaurant["name"]
        restaurant_category = restaurant["category"]
        restaurant_state = "activated" if restaurant["state"] == True else "disabled"
        print(f"- {restaurant_name.ljust(16)} | {restaurant_category.ljust(16)} | {restaurant_state}")
    return_to_the_main_menu()

def change_restaurant_state():
    shows_subtitles("Restaurant state")
    restaurant_name = input("Enter the name of the restaurant whose state you want to change: ")
    search_restaurant = False
    for restaurant in restaurant_lists:
        if restaurant_name == restaurant["name"]:
            search_restaurant = True
            restaurant["state"] = not restaurant["state"]
            message = f"The restaurant {restaurant_name} active with successfully!" if restaurant["state"] == True else f"The restaurant {restaurant_name} deactivated with successfully!"
            print(message)
    if search_restaurant != True:
        print(f"The restaurant {restaurant_name} wasn't found!")
    return_to_the_main_menu() 


def finish_app():
    shows_subtitles("Program finished with successfully!")

def choosen_option():
    try:
        choose_option = int(input("\nChoose an option: "))
        match choose_option:
            case 1:
                registers_new_restaurant()
            case 2:
                list_of_registered_restaurants()
            case 3:
                change_restaurant_state()
            case 4:
                finish_app()
            case _:
                invalid_option()
    except:
        print("Invalid option. Enter a valid number!")

def main_menu():
    shows_subtitles("Fast Food")
    show_options_of_the_main_menu()
    choosen_option()

if __name__ == "__main__":
    main_menu()