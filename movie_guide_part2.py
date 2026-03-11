# Stephanie Brainard
# CIS 261
# Week 6 - Movie Guide Part 2

#Shows the heading
def display_heading():
    print("*" * 30)
    print("Stephanie's Movie List Program")
    print("*" * 30)


#Shows the menu options to the user
def display_menu(): 
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")


#Reads the movies from the text file and adds them to a list
def get_titles():
    movie_list = []
    with open("movies.txt", "r") as txt:
        for line in txt:
            movie_list.append(line.strip())
        return movie_list
    print()


#Shows the movies in the list to the user with a number for each movie
def show_titles(movie_list):
    for i, titles in enumerate(movie_list, start=1):
        print(f"{i}. {titles}")
    print()
        

#Adds a movie to the list and shows a message that the movie was added. 
#If the user enters "c", the function will return to the menu without adding a movie.        
def add_titles(movie_list):
    movie = input("\nEnter a movie (or c to cancel): ") 
    if movie == "c":
        print()
        display_menu()
        return False
        

    elif movie_list.append(movie):
        print(f"{movie} added.\n")
        print()
        return True
    
    
#Writes the movies in the list to the text file, one movie per line.
def write_titles(movie_list):   
    with open("movies.txt", "w") as txt:
        for add in movie_list:
            txt.write(add.strip() + '\n')
          

 #Deletes a movie from the list and shows a message that the movie was removed. 
 #If the user enters "c", the function will return to the menu without deleting a movie           
def delete_titles(movie_list):
    if not movie_list:
        print("There are no movies to delete.")
        print()
   
    show_titles(movie_list)
    print()
    choice = input("Enter the movie number to remove (or c to cancel): ")
    print()

    if choice == "c":
        display_menu()
        return False
    
    try:
        movieChoice = int(choice)
    except ValueError:
        print("Invalid movie number. please enter the number that corresponds with the movie you want to select.")
        return False
        
    if 1 <= movieChoice <= len(movie_list):
        movieRem = movie_list.pop(movieChoice - 1)
        print(f"{movieRem} has been removed.")
        return True
    else:
        print("Invalid choice. Please try again.\n")
        return False
            
#The main function that runs the program and calls the other functions as needed. 
#It also handles the user input for the menu options and calls the appropriate functions 
#based on the user's choice.          
def main():
    display_heading()
    
    movie_list = get_titles()
    
    display_menu()
    print("\n")
    
        
    while True:
        
        menuSelect = input("Enter a Command: ").lower().strip()
        
        if menuSelect not in ("list", "add", "del", "exit"):
            print("Please enter a valid command.")
            
   
        if menuSelect == "list":
            print(F"Command: {menuSelect}")
            show_titles(movie_list)

        
        elif menuSelect == "add":
            print(F"Command: {menuSelect}")
            add_titles(movie_list)
            write_titles(movie_list)
            print()
        
        elif menuSelect == "del":
            print(F"Command: {menuSelect}")
            removed = delete_titles(movie_list)
            if removed:
                write_titles(movie_list)
            print()
        

        elif menuSelect.lower().strip() == "exit":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()



    