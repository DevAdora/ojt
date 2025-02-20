import random

quotes_dict = {}
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
    print("All Authors and their Quotes:")
    authors_dict = {}
    for key, (quote, author) in quotes_dict.items():
        if author not in authors_dict:
            authors_dict[author] = []
        authors_dict[author].append((key, quote))
    for author, quotes in authors_dict.items():
        print(f"{author}:")
        for key, quote in quotes:
            print(f"    {key}: \"{quote}\"")
    
    search_term = input("Enter the exact author name or the key ID to delete: ")
    if search_term.isdigit(): 
        key_id = int(search_term)
        if key_id in quotes_dict:
            _, author = quotes_dict[key_id]
            quotes_to_delete = [key for key, (quote, a) in quotes_dict.items() if a.lower() == author.lower()]

            print(f"All quotes by {author}:")
            for key in quotes_to_delete:
                quote, author = quotes_dict[key]
                print(f"{key}: \"{quote}\" by {author}")
                
            confirm = input(f"Are you sure you want to delete all quotes by {author}? (yes/no): ").lower()
            if confirm in ["yes", "y"]:
                for key in quotes_to_delete:
                    quote, author = quotes_dict[key]
                    del quotes_dict[key]
                    print(f"Quote \"{quote}\" by {author} has been deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print("Quote ID cannot be found.")
    else: 
        found = False
        if search_term in authors_dict:
            found = True
            print(f"All quotes by {search_term}:")
            for key, quote in authors_dict[search_term]:
                print(f"{key}: \"{quote}\" by {search_term}")
                
            confirm = input(f"Are you sure you want to delete all quotes by {search_term}? (yes/no): ").lower()
            if confirm in ["yes", "y"]:
                for key in authors_dict[search_term]:
                    key_id, quote = key
                    del quotes_dict[key_id]
                print(f"All quotes by {search_term} have been deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print("Author cannot be found.")

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
    print("All Authors and their Quotes:")
    authors_dict = {}
    for key, (quote, author) in quotes_dict.items():
        if author not in authors_dict:
            authors_dict[author] = []
        authors_dict[author].append((key, quote))
    for author, quotes in authors_dict.items():
        print(f"{author}:")
        for key, quote in quotes:
            print(f"    {key}: \"{quote}\"")
    
    search_term = input("Enter the exact author name or the key ID to update: ")
    if search_term.isdigit(): 
        key_id = int(search_term)
        if key_id in quotes_dict:
            _, author = quotes_dict[key_id]
            quotes_to_update = [key for key, (quote, a) in quotes_dict.items() if a.lower() == author.lower()]

            print(f"UPDATING {author}:")
            for key in quotes_to_update:
                quote, author = quotes_dict[key]
                print(f"{key}: \"{quote}\" by {author}")
                
            confirm = input(f"Are you sure you want to update {author}? (yes/no): ").lower()
            if confirm in ["yes", "y"]:
                new_author = input("Enter the new author name: ")
                for key in quotes_to_update:
                    quote, author = quotes_dict[key]
                    quotes_dict[key] = (quote, new_author)
                    print(f"Quote \"{quote}\" by {author} has been updated to \"{new_author}\".")
            else:
                print("Update cancelled.")
        else:
            print("Quote ID cannot be found.")
    else: 
        found = False
        if search_term in authors_dict:
            found = True
            print(f"All quotes by {search_term}:")
            for key, quote in authors_dict[search_term]:
                print(f"{key}: \"{quote}\" by {search_term}")
                
            confirm = input(f"Are you sure you want to update {search_term}? (yes/no): ").lower()
            if confirm in ["yes", "y"]:
                new_author = input("Enter the new author name: ")
                for key in authors_dict[search_term]:
                    key_id, quote = key
                    quotes_dict[key_id] = (quote, new_author)
                print(f"All quotes by {search_term} have been updated to \"{new_author}\".")
            else:
                print("Update cancelled.")
        else:
            print("Author cannot be found.")

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
            for key, (quote, author) in quotes_dict.items():
                print(f"{key}: \"{quote}\" by {author}")
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
