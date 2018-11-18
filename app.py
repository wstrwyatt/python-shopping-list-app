shopping_list = []
    
def add_to_list(item):
    #add item to the list
    shopping_list.append(item)
    #Notify user that the item was added, with current items in list
    print("Item added to list!")
    print("There are {} items on the list.".format(len(shopping_list)))
    

def show_help():
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help.
    Enter 'SHOW' for the shopping list.
    """)

    
def show_list():
    print("Here is your shopping list: ")
    for item in shopping_list:
        print(item)


show_help()
    
while True:
    new_item = input("> ")
    
    if new_item == "DONE":
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    
    add_to_list(new_item)
    
show_list()
