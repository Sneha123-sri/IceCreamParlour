
# 🍦 Ice Cream Cafe Management System

A simple and modular Ice Cream Cafe database application built using Python and SQLite. This CLI-based system lets customers suggest new flavours, manage allergens, ingredients, and shopping cart, and allows admins to manage flavours and inventory.

---

## 📁 Project Structure

| File Name           | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `iceCreamCafedb.py` | Initializes the SQLite database and sets up all required tables and data.   |
| `customer.py`       | Contains the `Customer` class for handling customer-related operations.     |
| `endUser.py`        | Contains the `EndUser` class that connects with Customer and provides features like flavour search, cart management, etc. |
| `main.py`           | Entry point of the application. Provides a menu-driven interface to interact with the system. |

---

## ⚙️ Features

### 🧑 Customer Actions
- Add a flavour suggestion
- View all suggestions
- Add allergens
- View allergens
- Add items to cart
- View cart
- Search for seasonal flavours

### 🛠️ Admin/Manager Actions
- Add new flavours
- View all flavours
- Add ingredients to inventory
- View ingredient inventory

## 🧪 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/Sneha123-sri/iceCreamCafe.git
cd iceCreamCafe
```

### 2. Run `iceCreamCafedb.py` to set up the database
```bash
python iceCreamCafedb.py
```

This will create `iceCreamCafe.db` and necessary tables.

### 3. Run the application
```bash
python main.py
```

---

## 🧾 Main Menu

When you run `main.py`, you'll see a menu like this:

```
Ice Cream Parlor Menu:
1. Add Customer Suggestion
2. View Customer Suggestion
3. Add Flavour
4. View Flavour
5. Add Ingredient
6. View Ingredient
7. Add Allergen
8. View Allergen
9. Add To Cart
10. View Cart
11. Search Flavours
12. Exit
```

Each option will ask for further input as needed and display results accordingly.

## ✅ Sample Actions

### Add a Suggestion
```
Enter your choice: 1
Enter your name: Sneha
Enter your suggestion: Rose Cardamom
✔ Suggestion added successfully!
Rose Cardamon was suggested by sneha

### Add to Cart
Enter your choice: 9
Enter flavour to add: Chocolate
✔ Chocolate added to cart!
Here the operations will be worked based on the choice they have given.
