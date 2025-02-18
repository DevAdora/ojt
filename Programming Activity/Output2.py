import random

quotes_dict = {}
quote_id = 1

def display_random_quote():
    selected_quote = random.choice(list(quotes_dict.values()))
    selected_quote_id = [key for key, value in quotes_dict.items() if value == selected_quote][0]
    quote, author = selected_quote
    print(f"Random Selected Quote: \"{quote}\" by {author} (ID: {selected_quote_id})")

while True:
    input_quote = input("Enter a quote: ")
    input_author = input("Enter the author: ")
    quotes_dict[quote_id] = (input_quote, input_author)
    quote_id += 1
    print("Quotes:")
    for key, (quote, author) in quotes_dict.items():
        print(f"{key}: \"{quote}\" by {author}")
    
    user_input = input(" -- Press 'R' to display a random quote\n -- Type 'Exit' to quit\n -- Press any key to continue: ").lower()
    if user_input == 'r':
        display_random_quote()
    elif user_input in ["exit", "yes", "y"]:
        display_random_quote()
        break
    else:
        continue