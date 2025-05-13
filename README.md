
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

---

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

This will create `iceCreamCafe.db` and initialize necessary tables.

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

Each option corresponds to a specific customer or admin operation.

---

## ✅ Sample Actions

### Add a Suggestion
```
Enter your choice: 1
Enter your name: Sneha
Enter your suggestion: Rose Cardamom
✔ Suggestion added successfully!
```

### Add to Cart
```
Enter your choice: 9
Enter flavour to add: Chocolate
✔ Chocolate added to cart!
```

---

## 📌 How It Works

When you run `main.py`, it presents a menu to the user. Based on the inputted choice (like `1`, `2`, `3`, etc.), the program internally:

- Uses the `EndUser` class (from `endUser.py`) for collecting user input and displaying results.
- Delegates business logic and database interactions to the `Customer` class (from `customer.py`).

This separation of logic (Customer) and interface (EndUser) keeps the application modular and easy to manage.

For example:
- If the user selects `1`, the `add_suggestion()` method from `EndUser` is called, which collects input and then calls `customer.add_suggestion()` from `customer.py`.
- Similarly, if the user selects `9`, it triggers `add_to_cart()` from `EndUser`, which again uses `Customer`’s logic to insert the flavour into the cart table in the SQLite database.

---

## 🐳 Docker Instructions

### 🔧 Build the Docker Image
```bash
docker build -t icecream-app .
```

### ▶️ Run the Application
```bash
docker run --rm icecream-app
```
