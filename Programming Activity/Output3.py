import random

def get_quotes():
    return [
        "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
        "In the middle of every difficulty lies opportunity. - Albert Einstein",
        "Do what you can, with what you have, where you are. - Theodore Roosevelt",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "Believe you can and you're halfway there. - Theodore Roosevelt"
    ]

def print_quotes(count=1):
    quotes = get_quotes()
    if count > len(quotes):
        count = len(quotes)  # Prevent exceeding available quotes
    
    selected_quotes = random.sample(quotes, count)
    for quote in selected_quotes:
        print(quote)

def main():
    try:
        num = int(input("How many quotes would you like to see? "))
        if num < 1:
            print("Please enter a positive number.")
        else:
            print_quotes(num)
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
