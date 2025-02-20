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

def main():
    while True:
        input_quote = input("Enter a quote: ")
        input_author = input("Enter the author: ")
        quotes_list.append((input_quote, input_author))
        print("Quotes:")
        for i, (quote, author) in enumerate(quotes_list, 1):
            print(f"{i}: \"{quote}\" by {author}")
        
        user_input = input(" -- Press 'D' to display quotes\n -- Press 'R' to randomly display a quote\n -- Type 'Exit' to quit\n -- Press any key to continue: ").lower()
        if user_input == 'd':
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
        else:
            continue

if __name__ == "__main__":
    main()
