print("Welcome to Coffee and Tea Guru.")

def drink_preference(drink, time):

    if drink == "coffee":
        if time == "morning":
            print("How about a cappuccino? You can have whatever coffee drink you like, with or without dairy.") 

        elif time == "afternoon":
            print("Have an espresso, americano or drip coffee and hold the milk!")

        else time == "night":
            print("Skip the coffee and have some water.")
            
    if drink == "water":
            print("Water is always a great option.")
        # return "Good morning! Feel free to enjoy any coffee you like, with or without milk. 
        #     You could have a cappuccino, a brew coffee with cream, a cafe au lait, a machiato. There are so many 
        #     delicious options!"
        #     else:
        #     return("Wonderful. Enjoy an espresso or other black coffee.")

    elif drink == "tea":
        if time == 'morning':
            print("Enjoy a black tea or a green tea, with or without milk.")

        elif time == "afternoon":
            print("Enjoy a green or herbal tea and hold the milk.")

        elif time == "night":
            print("Enjoy an herbal tea and hold the milk.")

    elif drink == "water":
        print("Water is always an excellent choice!")            

valid_drinks = ["coffee", "tea", "water"]
valid_drink = False
while valid_drink is False:
    drink = input("Would you like coffee or tea?")
    if drink in valid_drinks:
        valid_drink = True

valid_times = ["morning", "afternoon", "night"]
valid_time = False
while valid_time is False:
    time = input("Will you be drinking this in the morning, afternoon or night?")
    if time in valid_times:
        valid_time = True
    
rec = drink_preference(drink, time)
# print("definitely go for: "  + rec)
