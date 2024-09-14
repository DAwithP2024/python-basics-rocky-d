# Products available in the store by category
products: dict[str, list[tuple[str, int]]] = {
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
# categories_indices: dict[str, int] = {category: idx for idx, category in enumerate(categories)}


def display_products(products_list: list[tuple[str, int | float]]) -> None:
    print('=== Products ===')
    for item, price in products_list:
        print(f"{item}: {price}")


def display_sorted_products(products_list: list[tuple[str, int | float]], sort_order: str) -> list[tuple[str, int | float]]:
    products_list_sorted = sorted(products_list, key=lambda product: product[1], reverse='desc' == sort_order)
    display_products(products_list_sorted)
    return products_list_sorted


def display_categories() -> int | None:
    print('=== Product Categories ===')
    for idx, category in enumerate(categories, start=1):
        print(f"{idx}. {category}")
    print()

    category_str = input(f"Please enter a category (an integer in [{1}, {len(categories)}]) >> ")
    if category_str.isdigit() and 0 <= int(category_str) - 1 < len(categories):
        category = int(category_str) - 1
    else:
        category = None
    print()
    return category


def add_to_cart(cart: list[tuple[str, int | float, int]], product: tuple[str, int | float], quantity: int) -> None:
    cart.append(product + (quantity, ))


def display_cart(cart: list[tuple[str, int | float, int]]) -> None:
    print('=== Cart ===')
    total_cost = 0
    for item, price, quantity in cart:
        tmp = price * quantity
        print(f"{item} - ${price} x {quantity} = ${tmp}")
        total_cost += tmp
    print(f"Total cost: ${total_cost}")


def generate_receipt(name: str, email: str, cart: list[tuple[str, int | float, int]], total_cost: int | float, address: str) -> None:
    pass


def validate_name(name: str) -> bool:
    return 1 == name.count(' ') and all(s.isalpha() for s in name.split(' '))


def validate_email(email: str) -> bool:
    return '@' in email


def main() -> None:
    print('Welcome to Rocky\'s online shopping store!')
    print()

    name_str = input('Please enter your name (First Name and Last Name separated by a space) >> ')
    while not validate_name(name_str):
        name_str = input('Please enter your name (First Name and Last Name separated by a space) >> ')
    name = name_str
    print()

    email_str = input('Please enter your email >> ')
    while not validate_email(email_str):
        email_str = input('Please enter your email >> ')
    email = email_str
    print()

    cart: list[tuple[str, int | float, int]] = []

    while True:
        category = display_categories()
        print()

        # category_str = input('Please enter a category >> ')
        # while not (category_str in categories_indices.keys() or category_str.isdigit() and 0 <= int(category_str) - 1 < len(categories)):
        #     category_str = input('Please enter a category >> ')
        # category = category_str if category_str in categories_indices.keys() else int(category_str) - 1
        # print()

        display_products(products[category])
        print()

        print('=== Options ===')
        print('1. Select a product to buy.')
        print('2. Sort the products according to the price.')
        print('3. Go back to the category selection.')
        print('4. Finish shopping.')
        print()

        choice_str = input('Please select an option (an integer in [1, 4]) >> ')
        while not (choice_str.isdigit() and 1 <= int(choice_str) <= 4):
            choice_str = input('Please select an option (an integer in [1, 4]) >> ')
        choice = int(choice)
        print()

        if 1 == choice:
            ...
        elif 2 == choice:
            ...
        elif 3 == choice:
            continue
        else:  # elif 4 == choice:
            if 0 == len(cart):
                print('Thank you for using our portal. Hope you buy something from us next time. Have a nice day!')
            else:
                generate_receipt(
                    name,
                    email,
                    cart,
                    sum(price * quantity for _, price, quantity in cart),
                    input('Please enter your address >> '),
                )
            break


if __name__ == "__main__":
    main()
