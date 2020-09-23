#!python
# non-repeating welcome message
print("Welcome...")
# defines a bool
boolean = False
# while boolean does not equal True
while boolean != True:
    # defines drink as the value of what input returns.
    drink = input("Coffee or Tea?") #input is a default func in python
    time = input("morning, afternoon or night?")
    #if drink does not equal "Coffee" or "Tea"
    if drink != "Coffee" or drink != "Tea": # *You can also add water and tequilla here
        # gives user a message, telling them what they did wrong
        print("sorry, what was that?")
        '''Note: It is very important not to confuse your users with 
           reaccuuring prompts or functions.'''
    # else if time does not equal our desired results
    elif time != "morning" or time != "afternoon" or time != "night":
        # send them threw the loop again
        print("sorry, what was that?")
        '''Stretch challenge: your users will have to still type in their
        desired drink, if they get the time wrong. What is a way that we 
        can improve this? -If you are feeling awesome, Also see if you can
        figure out how to test a variable against a array of strings.'''
    # else our user input the desired inputs
    else:
        # so end the loop
        boolean = True