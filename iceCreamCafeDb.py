import sqlite3

connection = sqlite3.Connection("iceCreamCafeDb.db")
con = connection.cursor()


con.execute("""CREATE TABLE IF NOT EXISTS seasonal_flavours
                (Seasonal_flavour_id INTEGER PRIMARY KEY AUTOINCREMENT,
                Seasonal_flavour_name VARCHAR(255))
        """)

con.execute("""CREATE TABLE IF NOT EXISTS ingredient_inventory
                (ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                ingredient_name VARCHAR(255),
                quantity INTEGER)
        """)

con.execute("""CREATE TABLE IF NOT EXISTS customer_suggestions (
                suggestion_id INTEGER PRIMARY KEY AUTOINCREMENT,
                suggested_flavour_name TEXT,
                suggested_by TEXT)
        """)


con.execute("""CREATE TABLE IF NOT EXISTS  allergy_concerns (
                allergy_id INTEGER PRIMARY KEY AUTOINCREMENT,
                allergen_name TEXT)
        """)

con.execute("""CREATE TABLE IF NOT EXISTS cart (
                favorite_id INTEGER PRIMARY KEY AUTOINCREMENT,
                flavour_name TEXT)
        """)

flavours = [
    ('Chocolate',), ('Dry fruits',), ('Butterscotch',), ('Strawberry',)
]
con.executemany("Insert into seasonal_flavours ( Seasonal_flavour_name ) VALUES (?)", flavours)

ingredients = [
    ('Berries',10, ), ('Strawberries', 9,),('Mango', 12,), ('Mango',15,), ('Sugar', 20,)
]
con.executemany("Insert into ingredient_inventory ( ingredient_name , quantity ) VALUES (?,?)", ingredients)

connection.commit()

connection.close()