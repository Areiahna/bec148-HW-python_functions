# Task 1: Write a function that lets the user add items to a list, make sure you ask the user what they would like to add (reminder: ensure the function has a parameter to receive the list). 
shopping_list = []    

def main(list):
    while True:
        ans = input('''
        Shopping list Maker
        What would you like to do?
        
        1. Make a list
        2. Remove an item from your list
        3. View Shopping list
        4. Quit

        ''')
        
        if (ans == "1"):
           add_item()
        elif (ans == '2'):
            delete_item()

        elif(ans == '3'):
            view_list()

        elif(ans == '4'):
            print(" Thanks for using my app!")
            break

def add_item():
    while True:
        ans = input("What would you like to add?: ")
        shopping_list.append(ans)
        ans = input('''
        Would you like to add another item?
        y - yes
        n - no
        ''')
        if ans == "y":
            continue
        else:
            break

        

def delete_item():
    item = input("Which item would you like to remove?: ")
    while True:
        try:
            shopping_list.remove(item)
        except ValueError:
            print(f"It looks like you don't have {item} on your list\n")
            break
        else:
            print(f"Successfully removed {item} from your list!\n")
            break
        finally:
            view_list()

def view_list ():
    print("Your current shopping list:")
    print("~"*25)
    for item in range(len(shopping_list)):
       print(f"- {shopping_list[item]}")

        
main(shopping_list)

  # elif ans 
        #     # Task 2: Include a feature to remove items from the list.
        #     print("="*50)
        #     remove_item = input("Would you like to remove an item from your list? (y/n): ")
        #     if (remove_item == "y"):
        #         print(shopping_list)
        #         remove = input("Which item would you like to remove?: ")
        #         for item in shopping_list:
        #             if (remove == item):
        #                 shopping_list.remove(item)
        #             else:
        #                 print("="*50) 
        #     break

    #   for item in shopping_list:
    #     if (ans == item):
    #         shopping_list.remove(item)
    #     else: 
    #         print("Sorry that's not on the list")
    #         break