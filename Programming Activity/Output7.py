import random

quotes_dict = {}
quote_id = 1

quotes_txt_path ="C:/Users/Cloud Account/GitLabs/ojt-python/Programming Activity/quotes.txt"

def get_next_quote_id():
    global quote_id
    try:
        with open(quotes_txt_path, "r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                last_id = int(last_line.split(":")[0])
                quote_id = last_id + 1
            else:
                quote_id = 1
    except FileNotFoundError:
        quote_id = 1


def display_random_quote():
    selected_quote = random.choice(list(quotes_dict.values()))
    quote, author = selected_quote
    print(f"Random Selected Quote: \"{quote}\" by {author}")

def display_selected_quotes(count):
    if count > len(quotes_dict):
        count = len(quotes_dict)
    selected_quotes = random.sample(list(quotes_dict.values()), count)
    for quote, author in selected_quotes:
        print(f"\"{quote}\" by {author}")

def search_quote(search_term, quotes_txt_path):
    found = False
    try:
        with open(quotes_txt_path, "r") as file:
            lines = file.readlines()
        
        for line in lines:
            if search_term.lower() in line.lower(): 
                print(line.strip()) 
                found = True
                
        if not found:
            print("Quote cannot be found.")
    except FileNotFoundError:
        print(f"Error: The file at {quotes_txt_path} was not found.")

def search_author(search_term):
    found = False
    for key, (quote, author) in quotes_dict.items():
        if search_term.lower() in author.lower():
            print(f"{key}: \"{quote}\" by {author}")
            found = True
    if not found:
        print("Author cannot be found.")

def delete_quote():
    print("All Quotes:")
    try:
        with open(quotes_txt_path, "r") as file:
            lines = file.readlines()

        for line in lines:
            print(line.strip())

        search_term = input("Enter the quote you want to delete or the quote ID: ")

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
    for key, (quote, author) in quotes_dict.items():
        if author not in authors_dict:
            authors_dict[author] = []
        authors_dict[author].append((key, quote))

    print("All Authors and their Quotes:")
    author_index = 1
    author_keys = {} 
    for author, quotes in authors_dict.items():
        author_keys[author_index] = author 
        print(f"{author_index}. {author}:")
        for _, quote in quotes:
            print(f"    - {quote}")
        author_index += 1

    search_term = input("Enter the exact author name or the key ID to delete: ")

    if search_term.isdigit(): 
        key_id = int(search_term)

        if key_id in author_keys:
            author_to_delete = author_keys[key_id]
            quotes_to_delete = [key for key, (quote, a) in quotes_dict.items() if a.lower() == author_to_delete.lower()]

            print(f"All quotes by {author_to_delete}:")
            for key in quotes_to_delete:
                quote, author = quotes_dict[key]
                print(f"{key}: \"{quote}\" by {author}")

            confirm = input(f"Are you sure you want to delete all quotes by {author_to_delete}? (yes/no): ").lower()
            if confirm in ["yes", "y"]:
                for key in quotes_to_delete:
                    quote, author = quotes_dict[key]
                    del quotes_dict[key]
                    print(f"Quote \"{quote}\" by {author} has been deleted.")
                refresh_quotes_dict()
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid author ID.")
    else:
        found = False
        matching_authors = []

        for author, quotes in authors_dict.items():
            if search_term.lower() in author.lower():
                matching_authors.append(author)
                found = True

        if found:
            print("\nSelect the number of the author you want to delete:")
            for idx, author in enumerate(matching_authors, 1):
                print(f"{idx}. {author}")

            author_selection = int(input("Enter the number corresponding to the author you want to delete: "))

            selected_author = matching_authors[author_selection - 1]
            quotes_to_delete = [key for key, (quote, a) in quotes_dict.items() if a.lower() == selected_author.lower()]
            print(f"DELETING {selected_author}:")
            for key in quotes_to_delete:
                quote, author = quotes_dict[key]
                print(f"{key}: \"{quote}\" by {author}")

            confirm = input(f"Are you sure you want to delete all quotes by {selected_author}? (yes/no): ").lower()
            if confirm in ["yes", "y"]:
                for key in quotes_to_delete:
                    quote, author = quotes_dict[key]
                    del quotes_dict[key]
                    print(f"Quote \"{quote}\" by {author} has been deleted.")
                refresh_quotes_dict()
            else:
                print("Deletion cancelled.")
        else:
            print("No authors found with that name or letter.")

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


def update_quote(quotes_txt_path):
    print("All Quotes:")
    try:
        with open(quotes_txt_path, "r") as file:
            lines = file.readlines()
        
        for line in lines:
            print(line.strip())
        
        search_term = input("Enter the quote you want to update or the quote ID: ")

        if search_term.isdigit():  
            quote_id = int(search_term)
            try:
                line_to_update = lines[quote_id - 1]
                confirm = input(f"Are you sure you want to update: {line_to_update.strip()} (yes/no): ").lower()
                if confirm in ["yes", "y"]:
                    new_quote = input("Enter the new quote: ")
                    new_author = input("Enter the new author: ")
                    lines[quote_id - 1] = f"{quote_id}: \"{new_quote}\" by {new_author}\n"  #
                    with open(quotes_txt_path, "w") as file:
                        file.writelines(lines)
                    print(f"Quote {quote_id} has been updated.")
                else:
                    print("Update cancelled.")
            except IndexError:
                print("Quote ID cannot be found.")
        else:  # Searching by part of the quote text
            found = False
            for idx, line in enumerate(lines):
                if search_term.lower() in line.lower():
                    print(f"Found: {line.strip()} (ID: {idx + 1})")
                    found = True

            if found:
                quote_id = int(input("Enter the ID of the quote you want to update: "))
                new_quote = input("Enter the new quote: ")
                new_author = input("Enter the new author: ")
                lines[quote_id - 1] = f"{quote_id}: \"{new_quote}\" by {new_author}\n"  # Update the line
                with open(quotes_txt_path, "w") as file:
                    file.writelines(lines)
                print(f"Quote {quote_id} has been updated.")
            else:
                print("Quote cannot be found.")
    except FileNotFoundError:
        print(f"Error: The file at {quotes_txt_path} was not found.")

def update_author():
    authors_dict = {}
    for key, (quote, author) in quotes_dict.items():
        if author not in authors_dict:
            authors_dict[author] = []
        authors_dict[author].append((key, quote))
    
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
    display_file_in_box(quotes_txt_path)

    while True:
        user_input = input("-------------------------------------------------------------------\n| -- Press 'A' to add Quotes and Author\n| -- Press 'D' to display quotes\n| -- Press 'R' to randomly display a quote\n| -- Press 'S' to search\n| -- Press 'U' to update quote or author\n| -- Type 'All' to display all list of quotes and author\n| -- Type 'Del' to delete quote or Author\n| -- Type 'Exit' to quit\n| -- Press any key to continue: ").lower()
        if user_input == 'a':
            input_quote = input("Enter a quote: ")
            input_author = input("Enter the author: ")
            quotes_dict[quote_id] = (input_quote, input_author)
            with open(quotes_txt_path, "a") as file:
                file.write(f"{quote_id}: \"{input_quote}\" by {input_author}\n")
            quote_id += 1
            display_file_in_box(quotes_txt_path)
            for key, (quote, author) in quotes_dict.items():
                print(f"{key}: \"{quote}\" by {author}")
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
                search_quote(search_term)
            elif search_option == 'a':
                search_term = input("Enter the author you want to search: ")
                search_author(search_term)
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
