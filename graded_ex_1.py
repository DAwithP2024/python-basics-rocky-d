Product = tuple[str, int | float]
CartItem = tuple[str, int | float, int]

# Products available in the store by category
products: dict[str, list[Product]] = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

categories: list[str] = list(products.keys())


def display_products(products_list: list[Product]) -> None:
    print('=== Products ===')
    for idx, (item, price) in enumerate(products_list, start = 1):
        print(f"({idx}) {item}: {price}")


def display_sorted_products(products_list: list[Product], sort_order: str) -> list[Product]:
    products_list_sorted = sorted(products_list, key=lambda product: product[1], reverse='desc' == sort_order)
    display_products(products_list_sorted)
    return products_list_sorted


def display_categories() -> int | None:
    print('=== Product Categories ===')
    for idx, category in enumerate(categories, start=1):
        print(f"({idx}) {category}")
    print()

    category_input = input(f"Please enter a category (an integer in [{1}, {len(categories)}]) >> ")
    result = int(category_input) - 1 if category_input.isdigit() and 1 <= int(category_input) <= len(categories) else None
    print()
    return result


def add_to_cart(cart: list[CartItem], product: Product, quantity: int) -> None:
    cart.append(product + (quantity,))


def display_cart(cart: list[CartItem]) -> None:
    print('=== Shopping Cart ===')
    total_cost = 0
    for item, price, quantity in cart:
        cost = price * quantity
        print(f"{item} - ${price} x {quantity} = ${cost}")
        total_cost += cost
    print(f"Total cost: ${total_cost}")


def generate_receipt(name: str, email: str, cart: list[CartItem], total_cost: int | float, address: str) -> None:
    print('=== Shopping Receipt ===')
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print('Items Purchased:')
    for item, price, quantity in cart:
        print(f"{quantity} x {item} - ${price} = ${price * quantity}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print('Your items will be delivered in 3 days.')
    print('Payment will be accepted upon delivery.')


def validate_name(name: str) -> bool:
    return 1 == name.count(' ') and all(s.isalpha() for s in name.split(' '))


def validate_email(email: str) -> bool:
    return '@' in email


def main() -> None:
    print('=' * 20)

    cart: list[CartItem] = []

    print('Hi! Welcome to Rocky\'s online shopping store!')
    print()

    name_input = input('Please enter your name (First Name and Last Name separated by a space) >> ')
    while not validate_name(name_input):
        name_input = input('Please enter your name (First Name and Last Name separated by a space) >> ')
    name = name_input
    print()

    email_input = input('Please enter your email >> ')
    while not validate_email(email_input):
        email_input = input('Please enter your email >> ')
    email = email_input
    print()

    category_input = display_categories()
    while category_input is None:
        category_input = display_categories()
    category = categories[category_input]
    display_products(products[category])
    print()

    while True:
        print('=== Options ===')
        print('1. Select a product to buy.')
        print('2. Sort the products according to the price.')
        print('3. Go back to the category selection.')
        print('4. Finish shopping.')
        print()

        option_input = input('Please select an option (an integer in [1, 4]) >> ')
        while not (option_input.isdigit() and 1 <= int(option_input) <= 4):
            option_input = input('Please select an option (an integer in [1, 4]) >> ')
        option = int(option_input)
        print()

        if 1 == option:
            product_input = input(f"Please select a product (an integer in [1, {len(products[category])}]) >> ")
            while not (product_input.isdigit() and 1 <= int(product_input) <= len(products[category])):
                product_input = input(f"Please select a product (an integer in [1, {len(products[category])}]) >> ")
            product = products[category][int(product_input) - 1]
            print()

            quantity_input = input('Please enter a quantity (a positive integer) >> ')
            while not (quantity_input.isdigit() and 1 <= int(quantity_input)):
                quantity_input = input('Please enter a quantity (a positive integer) >> ')
            quantity = int(quantity_input)
            print()

            add_to_cart(cart, product, quantity)
        elif 2 == option:
            print('=== Sorting Order ===')
            print('(1) Ascending order.')
            print('(2) Descending order.')
            print()

            sortorder_input = input('Please select an option (an integer in [1, 2]) >> ')
            while not (sortorder_input.isdigit() and 1 <= int(sortorder_input) <= 2):
                sortorder_input = input('Please select an option (an integer in [1, 2]) >> ')
            sortorder = int(sortorder_input)
            print()

            products[category] = display_sorted_products(products[category], 'asc' if 1 == sortorder else 'desc')
            print()
        elif 3 == option:
            category_input = display_categories()
            while category_input is None:
                category_input = display_categories()
            category = categories[category_input]
            display_products(products[category])
            print()
        else:  # elif 4 == option:
            if 0 == len(cart):
                print('Thank you for using our portal.')
                print('Hope you buy something from us next time.')
                print('Have a nice day!')
                print()
            else:  # elif 0 < len(cart):
                display_cart()
                print()

                total_cost = sum(price * quantity for _, price, quantity in cart)
                address = input('Please enter your address >> ')
                generate_receipt(name, email, cart, total_cost, address)
                print()
            break
    print('=' * 20)


if __name__ == "__main__":
    main()
