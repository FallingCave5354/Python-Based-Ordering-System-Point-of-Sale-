####################################################
#   Python Based Ordering System (Point of Sale)   #
####################################################

# Inventory
class BaseStore:
    store_name = "iMark Bookstore"

class StoreData(BaseStore):
    inventory = [
        {"name": "Notebook", "price": 45.0, "qty": 87},
        {"name": "Ballpen", "price": 12.5, "qty": 134},
        {"name": "Pencil", "price": 8.0, "qty": 121},
        {"name": "Eraser", "price": 5.0, "qty": 44},
        {"name": "Ruler", "price": 15.0, "qty": 35},
        {"name": "Crayons", "price": 60.0, "qty": 31},
        {"name": "Bond Paper", "price": 1.0, "qty": 512},
        {"name": "Glue", "price": 18.0, "qty": 14},
        {"name": "Scissors", "price": 35.0, "qty": 19},
        {"name": "Backpack", "price": 550.0, "qty": 3},
    ]

class User:
    def admin(self):
        while True:
            show_inventory(store.inventory)
            print("\n[A] Add New | [E] Edit | [D] Delete | [Q] Logout")
            action = input("Select: ").lower()

            if action == 'q': break
            elif action == 'a': # New Item
                name = input("New name: ")
                price = float(input("Price: "))
                qty = int(input("Qty: "))
                store.inventory.append({"name": name, "price": price, "qty": qty})
            
            elif action in ['e', 'd']:
                idx = int(input("Enter item # to modify: ")) - 1
                if 0 <= idx < len(store.inventory):
                    if action == 'd': # Delete Item
                        deleted_item = store.inventory.pop(idx)
                        print(f"Removed {deleted_item['name']}.")
                    else: # Edit Item
                        store.inventory[idx]['name'] = input("New name: ")
                        store.inventory[idx]['price'] = float(input("New price: "))
                        store.inventory[idx]['qty'] = int(input("New qty: "))
                        print("Update successful!")
                else: print("Invalid number.")

    
    def cashier(self):
        cart = []
        while True:
            show_inventory(store.inventory)
            action = input("\nEnter item # to buy | [C] Checkout | [Q] Logout \n> ").lower()
            if action == 'q': break
            elif action == 'c':
                process_receipt(cart)
                break
            elif action.isdigit():
                idx = int(action) - 1
                if 0 <= idx < len(store.inventory):
                    it = store.inventory[idx]
                    buy_qty = int(input(f"How many {it['name']}? "))
                    if it['qty'] >= buy_qty:
                        it['qty'] -= buy_qty
                        cart.append({"name": it['name'], "price": it['price'], "qty": buy_qty})
                    else: print("Low stock!")

# Login
def auth(auth_user, valid_username, valid_password):
    print(f'\n===== Login as {auth_user} =====\n')
    username = input(f'{"Username: ":>15}')
    password = input(f'{"Password: ":>15}')
    return username == valid_username and password == valid_password

# Inventory Display
def show_inventory(items):
    print(f"\n{'-'*8} {StoreData.store_name} Inventory {'-'*8}")
    print(f"{'Item':^25} {'Price':<11} {'Stock'}")
    for i in range(len(items)):
        it = items[i]
        print(f"{i+1}. {it['name']:<{25 - len(str(i+1)) - 2}} P{it['price']:<10} {it['qty']}")

# Receipt
def process_receipt(cart):
    if not cart: return print("Cart is empty.")
    print("\n----- OFFICIAL RECEIPT -----\n")
    total = 0
    for i in range(len(cart)):
        item = cart[i]
        sub = item['price'] * item['qty']
        total += sub
        print(f"{item['name']} x{item['qty']} = P{sub}")
    print(f"TOTAL BILL: P{total}\n")

# Main System
store = StoreData()
menu = User()

while True:
    print(f"\n===== {store.store_name} =====")
    user = input("[1] Admin  \n[2] Cashier  \n[3] Exit \n> ")

    if user == '1': # Admin Menu
        if auth('Admin', 'admin', 'admin'):
            menu.admin()
        else: print('\nLogin Failed!')

    elif user == '2': # Cashier Menu
        if auth('Cashier', 'user', 'user'):
            menu.cashier()
        else: print('\nLogin Failed!')

    elif user == '3': # Back to Main Menu
        print("Shutting down...")
        break