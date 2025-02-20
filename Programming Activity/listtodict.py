import random

quotes_list = []
quotes_dict = {}
print("List to dictionary conversion")
while True:
    input_quote = input("Enter a quote: ")
    quotes_list.append(input_quote)
    print("Quotes:")
    for i, quote in enumerate(quotes_list, 1):
        print(f"{i}: {quote}")
    
    if input("Exit? (Yes/Y) ---- ").lower() in ["yes", "y"]:
        # Convert list to dictionary
        quotes_dict = {i+1: quote for i, quote in enumerate(quotes_list)}
        selected_quote = random.choice(list(quotes_dict.values()))
        selected_quote_id = [key for key, value in quotes_dict.items() if value == selected_quote][0]
        print(f"Random Selected Quote: {selected_quote} (ID: {selected_quote_id})")
        break
    else:
        continue