import random
quotes_dict = {}
quote_id = 1
quotes_txt_path ="C:/Users/Cloud Account/GitLabs/ojt-python/Programming Activity/quotes.txt"




def get_next_quote_id():
    global quote_id
    try:
        with open(quotes_txt_path, "r") as file:
            lines = file.readlines()
        
        max_id = 0
        for line in lines:
            parts = line.split(":")
            if len(parts) > 1:
                current_id = int(parts[0].strip())
                max_id = max(max_id, current_id)
        
        quote_id = max_id + 1
    except FileNotFoundError:
        quote_id = 1


def refresh_quotes_dict():
    """Rebuild quotes_dict and update the quote_id after a delete operation."""
    global quote_id
    quotes_dict.clear()
    get_next_quote_id()  

    try:
        with open(quotes_txt_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                parts = line.split(":")
                if len(parts) > 1:
                    current_id = int(parts[0].strip())
                    quote, author = parts[1].split(" by ")
                    quotes_dict[current_id] = (quote.strip().strip('"'), author.strip())
            get_next_quote_id()
    except FileNotFoundError:
        print("Quotes file not found!")
        
def display_selected_quotes(num):
    try:
        with open(quotes_txt_path, "r") as file:
            lines = file.readlines()
        
        quotes = []
        for line in lines:
            parts = line.split(":")
            if len(parts) > 1:
                quote, author = parts[1].split(" by ")
                quotes.append((quote.strip().strip('"'), author.strip()))
        
        if quotes:
            if num > len(quotes):
                print(f"There are only {len(quotes)} quotes available.")
                num = len(quotes)
            selected_quotes = random.sample(quotes, num)
            for quote, author in selected_quotes:
                print(f"\"{quote}\" by {author}")
        else:
            print("No quotes available to display.")
    except FileNotFoundError:
        print(f"Error: The file at {quotes_txt_path} was not found.")
        
        
def display_random_quote():
    try:
        with open(quotes_txt_path, "r") as file:
            lines = file.readlines()
        
        quotes = []
        for line in lines:
            parts = line.split(":")
            if len(parts) > 1:
                quote, author = parts[1].split(" by ")
                quotes.append((quote.strip().strip('"'), author.strip()))
        
        if quotes:
            selected_quote = random.choice(quotes)
            quote, author = selected_quote
            print(f"Random Selected Quote: \"{quote}\" by {author}")
        else:
            print("No quotes available to display.")
    except FileNotFoundError:
        print(f"Error: The file at {quotes_txt_path} was not found.")

        
def add_new_quote():
    """Function to add a new quote."""
    global quote_id
    refresh_quotes_dict()  
    
    input_quote = input("Enter a quote: ")
    input_author = input("Enter the author: ")
    quotes_dict[quote_id] = (input_quote, input_author)
    with open(quotes_txt_path, "a") as file:
        file.write(f"{quote_id}: \"{input_quote}\" by {input_author}\n")
    quote_id += 1
    display_file_in_box(quotes_txt_path)

    # Print all quotes
    #for key, (quote, author) in quotes_dict.items():
        #print(f"{key}: \"{quote}\" by {author}")
        
        
def delete_quote():
    print("All Quotes:")
    try:
        #Reading the files and the lines
        with open(quotes_txt_path, "r") as file:
            lines = file.readlines()
        for line in lines:
            print(line.strip())

        search_term = input("Enter the quote you want to delete or the quote ID: ")
        #If the search term is a digit or the ID
        if search_term.isdigit(): 
            quote_id_to_delete = int(search_term)
            try:
                line_to_delete = lines[quote_id_to_delete - 1]  
                confirm = input(f"Are you sure you want to delete: {line_to_delete.strip()} (yes/no): ").lower()
                if confirm in ["yes", "y"]:
                    del lines[quote_id_to_delete - 1] 
                    print(f"Quote {quote_id_to_delete} has been deleted.")
                    with open(quotes_txt_path, "w") as file:
                        file.writelines(lines)
                    refresh_quotes_dict()
                else:
                    print("Deletion cancelled.")
            except IndexError:
                print("Quote ID cannot be found.")
        else:  
            found = False
            for line in lines:
                if search_term.lower() in line.lower():
                    print(f"Found: {line.strip()}")
                    found = True
            if found:
                confirm = input("Are you sure you want to delete this quote? (yes/no): ").lower()
                if confirm in ["yes", "y"]:
                    lines = [line for line in lines if search_term.lower() not in line.lower()]
                    print(f"Quote containing '{search_term}' has been deleted.")
                    with open(quotes_txt_path, "w") as file:
                        file.writelines(lines)
                    refresh_quotes_dict()
                else:
                    print("Deletion cancelled.")
            else:
                print("Quote cannot be found.")
    except FileNotFoundError:
        print(f"Error: The file at {quotes_txt_path} was not found.")

def delete_author():
    authors_dict = {}
    try:
        with open(quotes_txt_path, "r") as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            parts = line.split(":")
            if len(parts) > 1:
                quote_id, quote_author = parts[0], parts[1].split(" by ")
                if len(quote_author) > 1:
                    author = quote_author[1].strip()
                    if author not in authors_dict:
                        authors_dict[author] = []
                    authors_dict[author].append((quote_id.strip(), parts[1].strip()))

        print("All Authors and their Quotes:")
        author_index = 1
        author_keys = {} 
        for author, quotes in authors_dict.items():
            author_keys[author_index] = author  
            print(f"{author_index}. {author}:")
            for quote in quotes:
                print(f"    - {quote[1]}")
            author_index += 1

        search_term = input("Enter the exact author name or the key ID to delete: ")

        if search_term.isdigit(): 
            key_id = int(search_term)
            if key_id in author_keys:
                author_to_delete = author_keys[key_id]
                confirm = input(f"Are you sure you want to delete all quotes by {author_to_delete}? (yes/no): ").lower()
                if confirm in ["yes", "y"]:
                    lines = [line for line in lines if f" by {author_to_delete}" not in line]
                    
                    with open(quotes_txt_path, "w") as file:
                        file.writelines(lines)

                    print(f"All quotes by {author_to_delete} have been deleted.")
                    refresh_quotes_dict()
                else:
                    print("Deletion cancelled.")
            else:
                print("Invalid author ID.")
        
        else:  
            found = False
            matching_authors = []

            for author in authors_dict:
                if search_term.lower() in author.lower():
                    matching_authors.append(author)
                    found = True

            if found:
                print("\nSelect the number of the author you want to delete:")
                for idx, author in enumerate(matching_authors, 1):
                    print(f"{idx}. {author}")

                author_selection = int(input("Enter the number corresponding to the author you want to delete: "))

                selected_author = matching_authors[author_selection - 1]
                confirm = input(f"Are you sure you want to delete all quotes by {selected_author}? (yes/no): ").lower()
                if confirm in ["yes", "y"]:
                    lines = [line for line in lines if f" by {selected_author}" not in line]

                    with open(quotes_txt_path, "w") as file:
                        file.writelines(lines)

                    print(f"All quotes by {selected_author} have been deleted.")
                    refresh_quotes_dict() 
                else:
                    print("Deletion cancelled.")
            else:
                print("No authors found with that name.")
    
    except FileNotFoundError:
        print("Error: The file at quotes.txt was not found.")

        
def update_quote(quotes_txt_path):
    print("All Quotes:")
    try:
        #Reading the files and the lines
        with open(quotes_txt_path, "r") as file:
            lines = file.readlines()
        
        for line in lines:
            print(line.strip())
        
        search_term = input("Enter the quote you want to update or the quote ID: ")


        #If the search term is a digit or the ID
        if search_term.isdigit(): 
            quote_id = int(search_term)
            try:
                line_to_update = lines[quote_id - 1]
                confirm = input(f"Are you sure you want to update: {line_to_update.strip()} (yes/no): ").lower()
                if confirm in ["yes", "y"]:
                    new_quote = input("Enter the new quote: ")
                    parts = line_to_update.split(" by ")
                    if len(parts) == 2:
                        author = parts[1]
                        lines[quote_id - 1] = f"{quote_id}: \"{new_quote}\" by {author}\n"
                    else:
                        lines[quote_id - 1] = f"{quote_id}: \"{new_quote}\"\n"
                    
                    with open(quotes_txt_path, "w") as file:
                        file.writelines(lines)
                    print(f"Quote {quote_id} has been updated.")
                else:
                    print("Update cancelled.")
            except IndexError:
                print("Quote ID cannot be found.")
                
        #If the search term is a string or a quote or the name
        else: 
            found = False
            for idx, line in enumerate(lines):
                if search_term.lower() in line.lower():
                    print(f"Found: {line.strip()} (ID: {idx + 1})")
                    found = True

            if found:
                quote_id = int(input("Enter the ID of the quote you want to update: "))
                new_quote = input("Enter the new quote: ")
                parts = lines[quote_id - 1].split(" by ")
                if len(parts) == 2:
                    author = parts[1]
                    lines[quote_id - 1] = f"{quote_id}: \"{new_quote}\" by {author}\n"
                else:
                    lines[quote_id - 1] = f"{quote_id}: \"{new_quote}\"\n"
                
                with open(quotes_txt_path, "w") as file:
                    file.writelines(lines)
                print(f"Quote {quote_id} has been updated.")
            else:
                print("Quote cannot be found.")
    except FileNotFoundError:
        print(f"Error: The file at {quotes_txt_path} was not found.")
def update_author():
    authors_dict = {}
    quotes_dict = {} 

    try:
        with open(quotes_txt_path, "r") as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            parts = line.split(":")
            if len(parts) > 1:
                quote_id, quote_author = parts[0], parts[1].split(" by ")
                if len(quote_author) > 1:
                    author = quote_author[1].strip()
                    quotes_dict[quote_id.strip()] = (quote_author[0].strip(), quote_author[1].strip())  # Storing quote_id and quote+author
                    if author not in authors_dict:
                        authors_dict[author] = []
                    authors_dict[author].append((quote_id.strip(), parts[1].strip()))
    
    except FileNotFoundError:
        print("Error: The file at quotes.txt was not found.")
        return

    print("All Authors and their Quotes:")
    author_index = 1
    author_keys = {}  
    for author, quotes in authors_dict.items():
        author_keys[author_index] = author 
        print(f"{author_index}. {author}:")
        for _, quote in quotes:
            print(f"    - {quote}")
        author_index += 1
    
    search_term = input("Enter the exact author name or the key ID to update: ")
    
    if search_term.isdigit(): 
        key_id = int(search_term)
        
        if key_id in author_keys:
            author_to_update = author_keys[key_id]
            quotes_to_update = [key for key, (quote, a) in quotes_dict.items() if a.lower() == author_to_update.lower()]
            
            print(f"UPDATING {author_to_update}:")
            for key in quotes_to_update:
                quote, author = quotes_dict[key]
                print(f"{key}: \"{quote}\" by {author}")
                
            confirm = input(f"Are you sure you want to update {author_to_update}? (yes/no): ").lower()
            if confirm in ["yes", "y"]:
                new_author = input("Enter the new author name: ")
                for key in quotes_to_update:
                    quote, author = quotes_dict[key]
                    quotes_dict[key] = (quote, new_author)
                    print(f"{author} has been updated to \"{new_author}\".")          
                try:
                    with open(quotes_txt_path, "w") as file:
                        for key, (quote, author) in quotes_dict.items():
                            file.write(f"{key}: \"{quote}\" by {author}\n")
                    print("Author update saved to file.")
                except Exception as e:
                    print(f"Error writing to file: {e}")
            else:
                print("Update cancelled.")
        else:
            print("Invalid author ID.")
    
    else: 
        found = False
        matching_authors = []

        for author, quotes in authors_dict.items():
            if search_term.lower() in author.lower():
                matching_authors.append(author)
                found = True
                print(f"{author}:")
                for key, quote in quotes:
                    print(f"    - {quote}")
        
        if found:
            print("\nSelect the number of the author you want to update:")
            for idx, author in enumerate(matching_authors, 1):
                print(f"{idx}. {author}")
            
            author_selection = int(input("Enter the number corresponding to the author you want to update: "))
            
            selected_author = matching_authors[author_selection - 1]
            quotes_to_update = [key for key, (quote, a) in quotes_dict.items() if a.lower() == selected_author.lower()]
            
            print(f"UPDATING {selected_author}:")
            for key in quotes_to_update:
                quote, author = quotes_dict[key]
                print(f"{key}: \"{quote}\" by {author}")
            
            confirm = input(f"Are you sure you want to update all quotes by {selected_author}? (yes/no): ").lower()
            if confirm in ["yes", "y"]:
                new_author = input("Enter the new author name: ")
                for key in quotes_to_update:
                    quote, author = quotes_dict[key]
                    quotes_dict[key] = (quote, new_author)
                    print(f"{author} has been updated to \"{new_author}\".")
                try:
                    with open(quotes_txt_path, "w") as file:
                        for key, (quote, author) in quotes_dict.items():
                            file.write(f"{key}: \"{quote}\" by {author}\n")
                    print("Author update saved to file.")
                except Exception as e:
                    print(f"Error writing to file: {e}")
            else:
                print("Update cancelled.")
        else:
            print("No authors found with that name or letter.")


def display_file_in_box(quotes_txt_path):
    try:
        with open(quotes_txt_path, "r") as file:
            content = file.read()

        box_width = 80  

        print("-------------------- Welcome to Quotes and Author Management System --------------------")
        print("|" + " " * (box_width + 6) + "|")
        print("|" + " " * (box_width + 6) + "|")
            
        lines = content.splitlines() 
            
        for line in lines:
            print("| " + line.ljust(box_width + 4) + " |")  

        print("|" + " " * (box_width + 4) + "  |")
        print("|" + " " * (box_width + 4) + "  |")
        print("-------------------- ********************************************** --------------------")

    except FileNotFoundError:
        print(f"Error: The file at {quotes_txt_path} was not found.")

def main():
    global quote_id
    global quotes_txt_path
    global get_next_quote_id
    refresh_quotes_dict()  # Ensure quotes are loaded from the file at the start
    display_file_in_box(quotes_txt_path)

    while True:
        user_input = input("-------------------------------------------------------------------\n| -- Press 'A' to add Quotes and Author\n| -- Press 'D' to display quotes\n| -- Press 'R' to randomly display a quote\n| -- Press 'S' to search\n| -- Press 'U' to update quote or author\n| -- Type 'All' to display all list of quotes and author\n| -- Type 'Del' to delete quote or Author\n| -- Type 'Exit' to quit\n| -- Press any key to continue: ").lower()
  
        if user_input == 'a': 
            add_new_quote()
        elif user_input == 'd':
            try:
                num = int(input("How many quotes would you like to see? "))
                if num < 1:
                    print("Please enter a positive number.")
                elif num > len(quotes_dict):
                    print("There are not enough quotes to display.")
                else:
                    display_selected_quotes(num)
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        elif user_input in ["exit", "yes", "y"]:
            break
        elif user_input in ["r", "random"]:
            display_random_quote()
        elif user_input in ["s", "search"]:
            search_option = input("-------------------------------------------------------------------\n| -- Press 'Q' to search for Quotes\n| -- Press 'A' to search for Authors\n| -- Press any key to continue: ").lower()
            if search_option == 'q':
                search_term = input("Enter the quote you want to search: ")
                #search_quote(search_term)
            elif search_option == 'a':
                search_term = input("Enter the author you want to search: ")
                #search_author(search_term)
        elif user_input in ["u", "update"]:
            update_option = input("-------------------------------------------------------------------\n| -- Press 'Q' to update Quotes\n| -- Press 'A' to update Authors\n| -- Press any key to continue: ").lower()
            if update_option == 'q':
                update_quote(quotes_txt_path)
            elif update_option == 'a':
                update_author()
        elif user_input in ["all", "list"]:
            print("All Quotes and Authors")
            display_file_in_box(quotes_txt_path)
           #for key, (quote, author) in quotes_dict.items():
                #print(f"{key}: \"{quote}\" by {author}")
        elif user_input in ["del", "delete"]:
            del_option = input("-------------------------------------------------------------------\n| -- Press 'Q' to delete Quotes\n| -- Press 'A' to delete Authors\n| -- Press any key to continue: ").lower()
            if del_option == 'q':
                delete_quote()  
            elif del_option == 'a':
                delete_author() 
        else:
            continue

if __name__ == "__main__":
    main()
