from customer import Customer
from endUser import EndUser

customer_instance = Customer()
endUser = EndUser(customer_instance)

actions = {
    '1': endUser.add_suggestion,
    '2': endUser.view_suggestions,
    '3': endUser.add_flavour,
    '4': endUser.view_flavours,
    '5': endUser.add_ingredient,
    '6': endUser.view_ingredients,
    '7': endUser.add_allergen,
    '8': endUser.view_allergens,
    '9': endUser.add_to_cart,
    '10': endUser.view_cart,
    '11': endUser.search_flavours,
}

while True:
    print("\nIce Cream Parlor Menu:")
    print("1. Add Customer Suggestion")
    print("2. View Customer Suggestion")
    print("3. Add Flavour")
    print("4. View Flavour")
    print("5. Add Ingredient")
    print("6. View Ingredient")
    print("7. Add Allergen")
    print("8. View Allergen")
    print("9. Add To Cart")
    print("10. View Cart")
    print("11. Search Flavours")
    print("12. Exit")

    choice = input("Enter your choice: ")

    if choice == '12':
        print("Goodbye!")
        break
    elif choice in actions:
        actions[choice]()
    else:
        print("Invalid choice. Please try again.")
