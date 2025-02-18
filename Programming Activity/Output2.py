import random

quotes_dict = {}
quote_id = 1

def display_random_quote():
    selected_quote = random.choice(list(quotes_dict.values()))
    selected_quote_id = [key for key, value in quotes_dict.items() if value == selected_quote][0]
    print(f"Random Selected Quote: {selected_quote} (ID: {selected_quote_id})")

while True:
    input_quote = input("Enter a quote: ")
    quotes_dict[quote_id] = input_quote
    quote_id += 1
    print(f"Quotes: {quotes_dict}")
    
    user_input = input("Press 'R' to display a random quote or 'Exit' to quit: ").lower()
    if user_input == 'r' or 'R':
        display_random_quote()
    elif user_input in ["exit", "yes", "y"]:
        display_random_quote()
        break
    else:
        continue