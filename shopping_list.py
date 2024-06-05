# Task 1: Write a function that lets the user add items to a list, make sure you ask the user what they would like to add (reminder: ensure the function has a parameter to receive the list). 
shopping_list = []    

def add_to_list (list):
    while True:
        item = input("What would you like to add to your shopping list?: ")
        shopping_list.append(item)
        add_item = input("Would you like to add another (y/n): ")
        if (add_item == "y"):
            pass
        elif (add_item !="y"):
            # Task 2: Include a feature to remove items from the list.
            print("="*50)
            remove_item = input("Would you like to remove an item from your list? (y/n): ")
            if (remove_item == "y"):
                print(shopping_list)
                remove = input("Which item would you like to remove?: ")
                for item in shopping_list:
                    if (remove == item):
                        shopping_list.remove(item)
                    else:
                        print("="*50) 
            break

        
add_to_list(shopping_list)

# Task 3: Add a function that prints out the entire list.
def view_list (list):
    print("Your shopping list:")
    for item in range(len(list)):
       print(f"- {list[item]}")
       
view_list(shopping_list)