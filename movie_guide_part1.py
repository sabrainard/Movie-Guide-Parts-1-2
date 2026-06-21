def display_heading():
    print("*" * 41)
    print("Stephanie's Stupendous Movie List Program")
    print("*" * 41)
    print()

def display_menu():  
    print("----COMMAND MENU----")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")

def display_movies(movie_list):
    for i, titles in enumerate(movie_list, start=1):
        print(f"{i}. {titles}")

def movie_add(movie_list): 
    movie = input("Enter a movie: ")
    movie_list.append(movie)
    
    print(f"{movie} added.\n")
    display_movies(movie_list)
       
def movie_del(movie_list):
    while True:
        display_movies(movie_list)
        movie_rem = None
        
        try:
            movie_choice =int(input("Enter the movie number to remove: "))
            
        except ValueError:
            print("Invalid movie number. please enter the number that corresponds with the movie you want to select.")
            continue
            
        if 1 <= movie_choice <= len(movie_list):
                movie_rem = movie_list.pop(movie_choice - 1)
                print(f"{movie_rem} has been removed.")
                print("Updated Moive List: ")
                display_movies(movie_list)
                break
        else:
                 print()
                 print("invalid movie number.")
                 
         
def main(): 
    movie_list = ["Dogma", "Mallrats", "Clerks", "Clerks 2" ]
    display_heading()
    print()
    
    while True:
        display_menu()
        print()

        menu_select = input("Enter a command: ")

        if menu_select.lower().strip() == "list":
            print(F"Command: {menu_select}")
            display_movies(movie_list)
            print()
        elif menu_select.lower().strip() == "add":
            print(F"Command: {menu_select}")
            movie_add(movie_list)
            print()
        elif menu_select.lower().strip() == "del":
            print(F"Command: {menu_select}")
            movie_del(movie_list)
            print()
        elif menu_select.lower().strip() == "exit":
            print("Goodbye!")
            break
        else:
            print("Not a valid command. Please try again")
            print()
    


if __name__ == "__main__":
    main()

