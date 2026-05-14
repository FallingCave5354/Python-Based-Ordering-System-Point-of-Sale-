# iMark Bookstore: Python-Based Ordering System (Point of Sale)
A lightweight, command-line interface (CLI) application designed to manage store inventory and process customer transactions. Built entirely in Python, this system uses role-based access control to separate administrative inventory management from cashier-facing sales operations.
## Features
### 🛠️ Admin Mode
The Admin menu provides full Control over the store's inventory.
 * **Add New:** Insert new items into the inventory with a specified name, price, and initial stock quantity.
 * **Edit:** Modify the details (name, price, or quantity) of any existing item.
 * **Delete:** Remove an item from the store's inventory entirely.
### 🛒 Cashier Mode
The Cashier menu is designed for daily sales operations.
 * **Browse Inventory:** View all available items, their prices, and current stock levels.
 * **Cart Management:** Add items to a shopping cart by specifying the item number and desired quantity.
 * **Stock Validation:** Automatically checks if there is sufficient stock before adding an item to the cart and prevents "Low stock!" transactions.
 * **Checkout & Receipt:** Calculates the subtotal for each item, displays the total bill, and generates an official receipt upon checkout.
## Prerequisites
To run this program, you will need:
 * **Python 3.x** installed on your system.
 * No external libraries are required (it runs on pure standard Python).
## How to Run
 1. Save the code to a file, for example: Python_Based_Ordering_System__Point_of_Sale_.py.
 2. Open your terminal or command prompt.
 3. Navigate to the directory where the file is saved.
 4. Execute the script using the following command:
   ```bash
   python Python_Based_Ordering_System__Point_of_Sale_.py
   
   ```
## System Credentials
The system includes pre-configured mock credentials for demonstration purposes. You must use these to log into the respective menus:
**Administrator Login**
 * **Username:** admin
 * **Password:** admin
**Cashier Login**
 * **Username:** user
 * **Password:** user
## Code Structure Overview
 * **BaseStore & StoreData**: Handles the initial configuration and the pre-populated list of items (dictionaries containing name, price, and qty).
 * **User**: Contains the core logic and loops for both the admin() and cashier() interfaces.
 * **auth()**: A helper function to validate login credentials against the hardcoded inputs.
 * **show_inventory()**: A helper function to print the current stock levels in a clean, formatted list.
 * **process_receipt()**: Calculates totals and prints the final bill for the cashier's checkout process.
