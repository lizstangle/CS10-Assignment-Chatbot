print("Welcome to Coffee and Tea Guru.")

def drink_preference(drink, time):

    if drink == "coffee":
        if time == "morning":
            return "How about a cappuccino? You can have whatever coffee drink you like, with or without dairy." 

        elif time == "afternoon":
            return "Have an espresso, americano or drip coffee and hold the milk!"
        elif time == "night":
            return "Skip the coffee and have some water."
        else:
            return "Water is always a great option."
        # return "Good morning! Feel free to enjoy any coffee you like, with or without milk. 
        #     You could have a cappuccino, a brew coffee with cream, a cafe au lait, a machiato. There are so many 
        #     delicious options!"
        #     else:
        #     return("Wonderful. Enjoy an espresso or other black coffee.")

    elif drink == "tea":
        if time == 'morning':
            return "Enjoy a black tea or a green tea, with or without milk."

        elif time == "afternoon":
            return "Enjoy a green or herbal tea and hold the milk."

        elif time == "night":
            return "Enjoy an herbal tea and hold the milk."

    elif drink == "water":
        return "Water is always an excellent choice!"            

valid_drinks = ["Coffee", "Tea", "Water"]
valid_drink = False
while valid_drink == False:
    drink = input("Would you like Coffee or Tea?")
    if drink in valid_drinks:
        valid_drink = True

valid_times = ["Morning", "Afternoon", "Night"]
valid_time = False
while valid_time == False:
    time = input("Will you be drinking this in the morning, afternoon or night?")
    if time in valid_times:
        valid_time = True
    
rec = drink_preference(drink, time)
print("definitely go for: "  + rec)
