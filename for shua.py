#step 1: create dictionary
dictionary = {"A": "Apple",
     "B": "Banana",
     "C": "Chiku",
     "D": "Durian"}
     
# exercise
while(True):
    
    print("1 - add,", "2 - search,", "3 - delete", "4 - end")
    selection = int(input("What do you want to do today? "))
    print("You have selected: ", selection)

    if selection == 1:
        print ("you have chosen to add definiton")
        key = input("Input key here: ")
        definition = input("Input definition here: ")
        dictionary[key] = definition
        print("Defintion added successfully")
        print(dictionary)
        
    elif selection == 2:
        print ("you have chosen to search definition")
        key = input("Which key?")
        if key in dictionary:
            print(dictionary[key])
        else: 
            print("definition not in dictionary", key)
            continue
        
    elif selection == 3:
        print("you have chosen to delete a definition")
        print(dictionary)
        key = input ("Which key and definition to delete? ")
        if key in dictionary:
            del dictionary[key] # new function
            print("successful deletion")
            print(dictionary)
        else: 
            print("key not found: ", key)
            continue
    elif selection == 4:
        print("Thank you")
        break
    
    elif (not(1 < selection < 5)):
        print("input is wrong")
        continue
        
