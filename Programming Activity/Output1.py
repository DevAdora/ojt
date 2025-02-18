import random
list = []
while True:
    input_list = input("Enter a quote: ")
    list.append(input_list)
    print(f"Quotes : {list}")
    print("Random Selected Quote: " + random.choice(list))
    if input("Exit? ---- ") == "Yes":
        break
    else:
        # print(f"Quotes : {list}")
        continue