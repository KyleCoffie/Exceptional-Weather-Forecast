#Task 1: Write a function that lets the user add items to a list.
grocery_list=[]
def add_items():

    while True:
        grocery_item = input("What is the item you would like to add ")
        grocery_list.append(grocery_item)
        add_grocery_item = (input("Do you want to add another item? (y or n) ")).lower()

        if add_grocery_item != 'y':
            break
    print ("Your grocery list is: ")
    for item in grocery_list:
        print(item)



#Task 2: Include a function to remove items from the list.

def remove_items():
    while True:
        grocery_item = input("What is the item you would you like to remove from the grocery list?  ")
        
        grocery_list.remove(grocery_item)
        remove_grocery_item = (input("Do you want to remove another item? (y or n) ")).lower()

        if remove_grocery_item != 'y':
            break
    print ("Your grocery list is: ")
    for item in grocery_list:
        print(item)

#Task 3: Add a function that prints out the entire list in a formatted way.

def print_items():
    print ("Your grocery list is: ")
    for item in grocery_list:
        print(f"Item is: {item}")


def menu():
   while True:
        print("""
        Menu:
        1. Add items
        2. Remove items
        3. Print items
        4. Quit
        """)
        option = int (input("what option would you like to use? ")) 
        if option ==1:
            add_items()
        elif option ==2:
            remove_items()
        elif option ==3:
            print_items()
        else:
            print("Thank you for using this program")
            break
menu()