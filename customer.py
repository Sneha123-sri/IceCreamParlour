import sqlite3


class Customer:
    def __init__(self, db="iceCreamCafeDb.db"):
        self.connection = sqlite3.connect(db)
        self.con = self.connection.cursor()

    def add_suggestion(self, flavour_name, suggested_by):
        self.con.execute("SELECT * FROM customer_suggestions WHERE suggested_flavour_name = ? AND suggested_by = ?",
                         (flavour_name, suggested_by))
        if self.con.fetchone():
            print(flavour_name," has already been suggested by ",suggested_by,". Duplicate not allowed.")
        else:
            self.con.execute("INSERT INTO customer_suggestions(suggested_flavour_name,suggested_by)  values (?,?)",
                             (flavour_name, suggested_by))
            print(flavour_name, " has been suggested by ", suggested_by)
            self.connection.commit()

    def view_suggestions(self):
        suggestions = self.con.execute("SELECT * FROM customer_suggestions")
        print("Sugestions are:")
        return suggestions

    def add_flavour(self, flavour_name):
        self.con.execute("SELECT * FROM seasonal_flavours WHERE Seasonal_flavour_name=?",
                         (flavour_name,))
        if self.con.fetchone():
            print(flavour_name, " has already exists. Duplicates not allowed.")
        else:
            self.con.execute("INSERT INTO seasonal_flavours(Seasonal_flavour_name)  values (?)",
                             (flavour_name,))
            print(flavour_name, " has been added ")
            self.connection.commit()

    def view_flavours(self):
        flavours = self.con.execute("SELECT * FROM seasonal_flavours")
        print("Available flavours are:")
        return flavours

    def add_ingredient(self, ingredient_name, quantity):
        self.con.execute("SELECT * FROM ingredient_inventory WHERE ingredient_name=?",
                         (ingredient_name,))
        if self.con.fetchone():
            print(ingredient_name, " has already exists. Duplicates not allowed.")
        else:
            self.con.execute("INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)",
                             (ingredient_name, quantity))
            self.connection.commit()
            print("Ingredient added successfully!")

    def view_ingredients(self):
        ingredients = self.con.execute("SELECT * FROM ingredient_inventory")
        return ingredients

    def add_allergen(self, allergen_name):
        self.con.execute("SELECT * FROM allergy_concerns WHERE allergen_name=?",
                         (allergen_name,))
        if self.con.fetchone():
            print(allergen_name, " has already exists. Duplicates not allowed.")
        else:
            self.con.execute("INSERT INTO allergy_concerns (allergen_name) VALUES (?)",
                             (allergen_name,))
            print(allergen_name, " has been added. ")
            self.connection.commit()

    def view_allergens(self):
        allergens = self.con.execute("SELECT * FROM allergy_concerns")
        return allergens

    def add_to_cart(self, flavour_name):
        self.con.execute("SELECT * FROM cart WHERE flavour_name=?",
                         (flavour_name,))
        if self.con.fetchone():
            print(flavour_name, " has already exists in the cart. Duplicates not allowed.")
        else:
            self.con.execute("SELECT Seasonal_flavour_name FROM seasonal_flavours WHERE Seasonal_flavour_name = ?",
                             (flavour_name,))
            if self.con.fetchone():
                self.con.execute("INSERT INTO cart (flavour_name) VALUES (?)", (flavour_name,))
                print(flavour_name, "has been added to cart.")
                self.connection.commit()
            else:
                print(flavour_name, "is not available in seasonal flavours. Please choose a different flavour.")

    def view_cart(self):
        cart_items = self.con.execute("SELECT * FROM cart")
        return cart_items

    def search_flavours(self, keyword):
        flavours=self.con.execute("SELECT * FROM seasonal_flavours WHERE Seasonal_flavour_name LIKE (?)",
                       ('%' + keyword + '%',))
        return flavours
