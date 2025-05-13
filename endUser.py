from customer import Customer


class EndUser:
    def __init__(self, customer):
        self.customer = customer

    def add_suggestion(self):
        flavour = input("Enter suggestion :")
        suggestion = input("Suggested Customer :")
        self.customer.add_suggestion(flavour, suggestion)

    def view_suggestions(self):
        suggestions = self.customer.view_suggestions()
        for i in suggestions:
            print(i)

    def add_flavour(self):
        flavour = input("Enter a flavour: ")
        self.customer.add_flavour(flavour)

    def view_flavours(self):
        flavours = self.customer.view_flavours()
        for i in flavours:
            print(i)

    def add_ingredient(self):
        ingredient_name = input("Enter ingredient name: ")
        quantity = int(input("Enter quantity: "))
        self.customer.add_ingredient(ingredient_name, quantity)

    def view_ingredients(self):
        ingredients = self.customer.view_ingredients()
        print("Ingredients:")
        for row in ingredients:
            print(row)

    def add_allergen(self):
        allergen_name = input("Enter allergen name: ")
        self.customer.add_allergen(allergen_name)

    def view_allergens(self):
        allergens = self.customer.view_allergens()
        print("Allergens:")
        for row in allergens:
            print(row)

    def add_to_cart(self):
        items=self.customer.view_flavours()
        for item in items:
            print(item)

        flavour_name = input("Enter flavour name to add to cart: ")
        self.customer.add_to_cart(flavour_name)

    def view_cart(self):
        cart_items = self.customer.view_cart()
        print("Cart items :")
        for i in cart_items:
            print(i)

    def search_flavours(self):
        keyword = input("Enter keyword to search: ")
        results = self.customer.search_flavours(keyword)
        print("Search results:")
        for row in results:
            print(row)

