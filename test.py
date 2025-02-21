#num1 = int(input())

#numbers = list(map(int, input().split()))

#result =  numbers[0] - numbers[1]

#print(f" {numbers[0]} - {numbers[1]} = {result}")



#list1 = list(map(int, input().split()))
#list2 = list(map(int, input().split()))

#if any(a == b for a, b in zip(list1, list2)):
 #   print("no")
 # #else:
# print("yes")




#def pyramid(rows=8):
 #   for i in range(rows):
 #       print (' '*(rows-i-1) + '*'*(2*i+1))

#pyramid(8)
  
#pyramid(12)
 



quotes_dict = {}

def search_quote(quote):
    found = False
    for key, (quote, author) in quotes_dict.items():
        if quote.lower() in quote.lower():
            print(f"Quote: {quote} Author: {author}")
            found = True
    if not found:
        print("Quote not found")
def search_author(author):
    found = False
    for key, (quote, author) in quotes_dict.items():
        if author.lower() in author.lower():
            print(f"Quote: {quote} Author: {author}")
            found = True
    if not found:
        print("Author not found")
while True:
    user_input = input("-------------------------------------------------------------------\n| -- Press 'A' to add Quotes and Author\n| -- Press 'S' to search\n| -- Type 'Exit' to quit\n| -- Press any key to continue: ").lower()
    if user_input == 'a':
        quote = input("Enter Quote: ")
        author = input("Enter Author: ")
        quotes_dict[quote] = quote, author
        print("Quote added successfully")
    elif user_input == 's':
        search_option = input("-------------------------------------------------------------------\n| -- Press 'Q' to search for Quotes\n| -- Press 'A' to search for Authors\n| -- Press any key to continue: ").lower()      
        if search_option == 'q':
            search_term = input("Enter the quote you want to search: ")
            search_quote(search_term)
        elif search_option == 'a':
            search_term = input("Enter the author you want to search: ")
            search_author(search_term)
        else:
            print("Quote not found")
    elif user_input == 'exit':
        break
    else:
        print("Invalid input. Please try again")
        


