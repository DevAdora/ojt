import random

quotes_dict = {}
quote_id = 1

quotes_txt_path ="C:/Users/Cloud Account/GitLabs/ojt-python/Programming Activity/quotes.txt"

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

def search_quote(search_term):
    found = False
    for key, (quote, author) in quotes_dict.items():
        if search_term.lower() in quote.lower():
            print(f"{key}: \"{quote}\" by {author}")
            found = True
    if not found:
        print("Quote cannot be found.")

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
    for key, (quote, author) in quotes_dict.items():
        print(f"{key}: \"{quote}\" by {author}")
    search_term = input("Enter the quote you want to delete or the key ID: ")
    
    if search_term.isdigit(): 
        key_id = int(search_term)
        if key_id in quotes_dict:
            quote, author = quotes_dict[key_id]
            confirm = input(f"Are you sure you want to delete the quote \"{quote}\" by {author}? (yes/no): ").lower()
            if confirm in ["yes", "y"]:
                del quotes_dict[key_id]
                print(f"Quote \"{quote}\" by {author} has been deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print("Quote ID cannot be found.")
    else: 
        found = False
        for key, (quote, author) in quotes_dict.items():
            if search_term.lower() in quote.lower():  
                print(f"{key}: \"{quote}\" by {author}")
                found = True
        if found:
            key_id = int(input("Enter the key ID of the quote you want to delete: "))
            if key_id in quotes_dict:
                quote, author = quotes_dict[key_id]
                confirm = input(f"Are you sure you want to delete the quote \"{quote}\" by {author}? (yes/no): ").lower()
                if confirm in ["yes", "y"]:
                    del quotes_dict[key_id]
                    print(f"Quote \"{quote}\" by {author} has been deleted.")
                else:
                    print("Deletion cancelled.")
            else:
                print("Quote ID cannot be found.")
        else:
            print("Quote cannot be found.")

def delete_author():
    # Group quotes by author
    authors_dict = {}
    for key, (quote, author) in quotes_dict.items():
        if author not in authors_dict:
            authors_dict[author] = []
        authors_dict[author].append((key, quote))
    
    # Display all authors with their quotes in the desired format
    print("All Authors and their Quotes:")
    author_index = 1
    author_keys = {}  # Store mapping of index to author
    for author, quotes in authors_dict.items():
        author_keys[author_index] = author  # Map index to author name
        print(f"{author_index}. {author}:")
        for _, quote in quotes:
            print(f"    - {quote}")
        author_index += 1
    
    # Prompt the user to select an author or key
    search_term = input("Enter the exact author name or the key ID to delete: ")
    
    if search_term.isdigit():  # Handle selecting by key ID
        key_id = int(search_term)
        
        # Find the author corresponding to the key_id
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
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid author ID.")
    
    else:  # Search by part of the author's name
        found = False
        matching_authors = []

        # Check if any author's name contains the search term
        for author, quotes in authors_dict.items():
            if search_term.lower() in author.lower():
                matching_authors.append(author)
                found = True
                #print(f"{author}:")
                #for key, quote in quotes:
                    #print(f"    - {quote}")
        
        if found:
            print("\nSelect the number of the author you want to delete:")
            for idx, author in enumerate(matching_authors, 1):
                print(f"{idx}. {author}")
            
            # Let the user select the number corresponding to the author
            author_selection = int(input("Enter the number corresponding to the author you want to delete: "))
            
            # Get the selected author
            selected_author = matching_authors[author_selection - 1]
            quotes_to_delete = [key for key, (quote, a) in quotes_dict.items() if a.lower() == selected_author.lower()]
            print(f"DELETING {selected_author}:")
            print(f"ALL WORKS by {selected_author}:")
            for key in quotes_to_delete:
                quote, author = quotes_dict[key]
                print(f"{key}: \"{quote}\" by {author}")
            
            confirm = input(f"Are you sure you want to delete all quotes by {selected_author}? (yes/no): ").lower()
            if confirm in ["yes", "y"]:
                for key in quotes_to_delete:
                    quote, author = quotes_dict[key]
                    del quotes_dict[key]
                    print(f"Quote \"{quote}\" by {author} has been deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print("No authors found with that name or letter.")


def update_quote():
    print("All Quotes:")
    for key, (quote, author) in quotes_dict.items():
        print(f"{key}: \"{quote}\" by {author}")
    search_term = input("Enter the quote you want to update or the key ID: ")
    
    if search_term.isdigit(): 
        key_id = int(search_term)
        if key_id in quotes_dict:
            quote, author = quotes_dict[key_id]
            confirm = input(f"Are you sure you want to update the quote \"{quote}\" by {author}? (yes/no): ").lower()
            if confirm in ["yes", "y"]:
                new_quote = input("Enter the new quote: ")
                quotes_dict[key_id] = (new_quote, author)
                print(f"Quote \"{quote}\" by {author} has been updated to \"{new_quote}\".")
            else:
                print("Update cancelled.")
        else:
            print("Quote ID cannot be found.")
    else: 
        found = False
        for key, (quote, author) in quotes_dict.items():
            if search_term.lower() in quote.lower():  
                print(f"{key}: \"{quote}\" by {author}")
                found = True
        if found:
            key_id = int(input("Enter the key ID of the quote you want to update: "))
            if key_id in quotes_dict:
                quote, author = quotes_dict[key_id]
                confirm = input(f"Are you sure you want to update the quote \"{quote}\" by {author}? (yes/no): ").lower()
                if confirm in ["yes", "y"]:
                    new_quote = input("Enter the new quote: ")
                    quotes_dict[key_id] = (new_quote, author)
                    print(f"Quote \"{quote}\" by {author} has been updated to \"{new_quote}\".")
                else:
                    print("Update cancelled.")
            else:
                print("Quote ID cannot be found.")
        else:
            print("Quote cannot be found.")

def update_author():
    # Group quotes by author
    authors_dict = {}
    for key, (quote, author) in quotes_dict.items():
        if author not in authors_dict:
            authors_dict[author] = []
        authors_dict[author].append((key, quote))
    
    # Display all authors with their quotes in the desired format
    print("All Authors and their Quotes:")
    author_index = 1
    author_keys = {}  # Store mapping of index to author
    for author, quotes in authors_dict.items():
        author_keys[author_index] = author  # Map index to author name
        print(f"{author_index}. {author}:")
        for _, quote in quotes:
            print(f"    - {quote}")
        author_index += 1
    
    # Prompt the user to select an author or key
    search_term = input("Enter the exact author name or the key ID to update: ")
    
    if search_term.isdigit():  # Handle selecting by key ID
        key_id = int(search_term)
        
        # Find the author corresponding to the key_id
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
    
    else:  # Search by part of the author's name
        found = False
        matching_authors = []

        # Check if any author's name contains the search term
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
            
            # Let the user select the number corresponding to the author
            author_selection = int(input("Enter the number corresponding to the author you want to update: "))
            
            # Get the selected author
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

def main():
    global quote_id
    while True:
        user_input = input("-------------------------------------------------------------------\n| -- Press 'A' to add Quotes and Author\n| -- Press 'D' to display quotes\n| -- Press 'R' to randomly display a quote\n| -- Press 'S' to search\n| -- Press 'U' to update quote or author\n| -- Type 'All' to display all list of quotes and author\n| -- Type 'Del' to delete quote or Author\n| -- Type 'Exit' to quit\n| -- Press any key to continue: ").lower()
        if user_input == 'a':
            input_quote = input("Enter a quote: ")
            input_author = input("Enter the author: ")
            quotes_dict[quote_id] = (input_quote, input_author)
            quote_id += 1
            print("Quotes:")
            for key, (quote, author) in quotes_dict.items():
                print(f"{key}: \"{quote}\" by {author}")
                with open(quotes_txt_path, "a") as file:
                    file.write(f"{key}: \"{quote}\" by {author}\n")
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
                update_quote()
            elif update_option == 'a':
                update_author()
        elif user_input in ["all", "list"]:
            print("All Quotes and Authors")
            file = open(quotes_txt_path, "r")
            print(file.read())
            file.close()
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
