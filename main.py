import random

print("Welcome to Coffee and Tea Guru.")

def drink_preference(drink, time):

    if drink == "coffee":
        if time == "morning":
            print("How about a cappuccino? You can have whatever coffee drink you like, with or without milk.") 

        elif time == "afternoon":
            print("Go for an espresso, americano or drip coffee and hold the milk!")

        elif time == "night":
            print("Skip the coffee and have some water.")

    if drink == "water":
            locations = ["while watching cinema of the caribean", 
                         "sailing in the caribean", 
                        "while dreaming of the caribean"]
            choice = random.randint(0, len(locations))
            print("Water is always an excellent choice, " + locations[choice])

    if drink == "tea":
        if time == 'morning':
            print("Enjoy a black tea or a green tea, with or without milk.")

        elif time == "afternoon":
            print("Enjoy a green or herbal tea and hold the milk.")

        elif time == "night":
            print("Enjoy an herbal tea and hold the milk.")



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
    
drink_preference(drink, time)
