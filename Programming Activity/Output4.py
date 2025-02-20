import random

quotes_dict = {}
quote_index = {}  # Maps words in quotes to their corresponding keys
author_index = {}  # Maps author names to their corresponding keys
quote_id = 1

def add_to_index(dictionary, key, value):
    for i in range(len(key)):
        substring = key[:i+1]
        if substring in dictionary:
            dictionary[substring].add(value)
        else:
            dictionary[substring] = {value}

def display_random_quote():
    if quotes_dict:
        quote, author = random.choice(list(quotes_dict.values()))
        print(f"Random Selected Quote: \"{quote}\" by {author}")
    else:
        print("No quotes available.")

def display_selected_quotes(count):
    count = min(count, len(quotes_dict))
    selected_quotes = random.sample(list(quotes_dict.values()), count)
    for quote, author in selected_quotes:
        print(f"\"{quote}\" by {author}")

def search_quote(search_term):
    found_keys = set()
    for key in quote_index:
        if search_term.lower() in key:
            found_keys.update(quote_index[key])
    
    if found_keys:
        for key in found_keys:
            quote, author = quotes_dict[key]
            print(f"{key}: \"{quote}\" by {author}")
    else:
        print("Quote cannot be found.")

def search_author(search_term):
    found_keys = set()
    for key in author_index:
        if search_term.lower() in key:
            found_keys.update(author_index[key])
    
    if found_keys:
        for key in found_keys:
            quote, author = quotes_dict[key]
            print(f"{key}: \"{quote}\" by {author}")
    else:
        print("Author cannot be found.")

def main():
    global quote_id
    while True:
        user_input = input("-------------------------------------------------------------------\n| -- Press 'A' to add Quotes and Author\n| -- Press 'D' to display quotes\n| -- Press 'R' to randomly display a quote\n| -- Press 'S' to search\n| -- Type 'Exit' to quit\n| -- Press any key to continue: ").lower()
        
        if user_input == 'a':
            input_quote = input("Enter a quote: ")
            input_author = input("Enter the author: ")
            
            quotes_dict[quote_id] = (input_quote, input_author)
            
            add_to_index(quote_index, input_quote.lower(), quote_id)
            add_to_index(author_index, input_author.lower(), quote_id)
            
            quote_id += 1
            
            print("Quotes:")
            for key, (quote, author) in quotes_dict.items():
                print(f"{key}: \"{quote}\" by {author}")
        
        elif user_input == 'd':
            try:
                num = int(input("How many quotes would you like to see? "))
                if num < 1:
                    print("Please enter a positive number.")
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
        
        else:
            continue

if __name__ == "__main__":
    main()
