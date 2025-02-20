import random

quotes_list = []

def display_random_quote():
    selected_quote = random.choice(quotes_list)
    quote, author = selected_quote
    print(f"Random Selected Quote: \"{quote}\" by {author}")

def display_selected_quotes(count):
    if count > len(quotes_list):
        count = len(quotes_list)
    selected_quotes = random.sample(quotes_list, count)
    for quote, author in selected_quotes:
        print(f"\"{quote}\" by {author}")

def search_quote(search_term):
    found = False
    for i, (quote, author) in enumerate(quotes_list, 1):
        if search_term.lower() in quote.lower():
            print(f"{i}: \"{quote}\" by {author}")
            found = True
    if not found:
        print("Quote cannot be found.")

def search_author(search_term):
    found = False
    for i, (quote, author) in enumerate(quotes_list, 1):
        if search_term.lower() in author.lower():
            print(f"{i}: \"{quote}\" by {author}")
            found = True
    if not found:
        print("Author cannot be found.")

def main():
    while True:
      
        
        user_input = input("-------------------------------------------------------------------\n| -- Press 'A' to add Quotes and Author\n| -- Press 'D' to display quotes\n| -- Press 'R' to randomly display a quote\n| -- Press 'S' to search\n| -- Type 'Exit' to quit\n| -- Press any key to continue: ").lower()
        if user_input == 'a':
            input_quote = input("Enter a quote: ")
            input_author = input("Enter the author: ")
            quotes_list.append((input_quote, input_author))
            print("Quotes:")
            for i, (quote, author) in enumerate(quotes_list, 1):
                print(f"{i}: \"{quote}\" by {author}")
        elif user_input == 'd':
            try:
                num = int(input("How many quotes would you like to see? "))
                if num < 1:
                    print("Please enter a positive number.")
                elif num > len(quotes_list):
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
        else:
            continue

if __name__ == "__main__":
    main()
