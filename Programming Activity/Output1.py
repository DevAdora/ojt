import random
list = []
while True:
    input_list = input("Enter a quote: ")
    list.append(input_list)
    print(f"Quotes : {list}")
    #print("Random Selected Quote: " + random.choice(list))
    user_input = input(" -- Type 'Exit' to quit\n -- Press any key to continue: ").lower()

    if user_input in ["exit", "yes", "y"]:
        print("Random Selected Quote: " + random.choice(list))
        break
    else:
        # print(f"Quotes : {list}")
        continue