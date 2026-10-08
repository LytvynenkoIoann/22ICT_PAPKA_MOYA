# Міні магазин у консолі

# Каталог товарів
products = {
    "Мишка": {"price": 800.00, "quantity": 6},
    "Клавіатура": {"price": 1500.00, "quantity": 4},
    "Навушники": {"price": 1200.00, "quantity": 8},
    "Монітор": {"price": 6500.00, "quantity": 3},
    "Флешка": {"price": 500.00, "quantity": 10}
}

# Кошик покупця
cart = {}

# Пароль адміністратора
admin_password = "1234"


# Перегляд каталогу
def show_catalog():
    print("\n===== КАТАЛОГ ТОВАРІВ =====")

    for name, product in products.items():
        price = product["price"]
        quantity = product["quantity"]

        if quantity > 0:
            print(f"{name} — {price:.2f}грн — {quantity} шт.")
        else:
            print(f"{name} — {price:.2f}грн — Немає в наявності")


# Додавання товару в кошик
def add_to_cart():
    show_catalog()

    name = input("\nВведіть назву товару: ")

    if name not in products:
        print("Такого товару немає в каталозі.")
        return

    try:
        amount = int(input("Введіть кількість: "))
    except ValueError:
        print("Кількість повинна бути числом.")
        return

    if amount <= 0:
        print("Кількість повинна бути більшою за 0.")
        return

    available = products[name]["quantity"]
    already_in_cart = cart.get(name, 0)

    if already_in_cart + amount > available:
        print("Немає в наявності такої кількості товару.")
        print(f"Доступно: {available - already_in_cart} шт.")
        return

    cart[name] = already_in_cart + amount

    print(f"Товар додано до кошика: {name} x{amount}")


# Перегляд кошика
def show_cart():
    print("\n===== КОШИК =====")

    if not cart:
        print("Кошик порожній.")
        return

    total = 0

    for name, amount in cart.items():
        price = products[name]["price"]
        cost = price * amount
        total += cost

        print(f"{name} — {amount} шт. — {cost:.2f}грн")

    print("--------------------------")
    print(f"Всього до сплати: {total:.2f}грн")


# Видалення товару з кошика
def remove_from_cart():
    if not cart:
        print("\nКошик порожній.")
        return

    show_cart()

    name = input("\nВведіть назву товару для видалення: ")

    if name not in cart:
        print("Цього товару немає у кошику.")
        return

    try:
        amount = int(input("Скільки видалити: "))
    except ValueError:
        print("Кількість повинна бути числом.")
        return

    if amount <= 0:
        print("Кількість повинна бути більшою за 0.")
        return

    if amount >= cart[name]:
        del cart[name]
        print("Товар повністю видалено з кошика.")
    else:
        cart[name] -= amount
        print(f"З кошика видалено {amount} шт. товару {name}.")


# Покупка товарів
def buy_products():
    if not cart:
        print("\nКошик порожній.")
        return

    show_cart()

    answer = input("\nПідтвердити покупку? (так/ні): ").lower()

    if answer != "так":
        print("Покупку скасовано.")
        return

    total = 0

    # Перевірка наявності всіх товарів
    for name, amount in cart.items():
        if amount > products[name]["quantity"]:
            print(f"Немає в наявності: {name}")
            return

    # Зменшення кількості товарів
    for name, amount in cart.items():
        products[name]["quantity"] -= amount
        total += products[name]["price"] * amount

    cart.clear()

    print("\nПокупку успішно здійснено!")
    print(f"Сума покупки: {total:.2f}грн")


# Вхід адміністратора
def admin_login():
    password = input("\nВведіть пароль адміністратора: ")

    if password != admin_password:
        print("Неправильний пароль.")
        return

    print("\nВхід адміністратора успішний!")

    while True:
        print("\n===== МЕНЮ АДМІНІСТРАТОРА =====")
        print("1. Переглянути залишки")
        print("2. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            show_stock()

        elif choice == "2":
            print("Вихід з режиму адміністратора.")
            break

        else:
            print("Невірний вибір.")


# Перегляд залишків адміністратором
def show_stock():
    print("\n===== ЗАЛИШКИ НА СКЛАДІ =====")

    # Lambda-функція для сортування товарів за назвою
    sorted_products = sorted(
        products.items(),
        key=lambda item: item[0]
    )

    for name, product in sorted_products:
        quantity = product["quantity"]

        if quantity >= 1:
            print(f"{name} — {quantity} шт.")
        else:
            print(f"{name} — Немає в наявності")


# Головне меню покупця
def customer_menu():
    while True:
        print("\n===== МАГАЗИН =====")
        print("1. Переглянути каталог")
        print("2. Додати товар у кошик")
        print("3. Переглянути кошик")
        print("4. Видалити товар з кошика")
        print("5. Купити товари з кошика")
        print("6. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            show_catalog()

        elif choice == "2":
            add_to_cart()

        elif choice == "3":
            show_cart()

        elif choice == "4":
            remove_from_cart()

        elif choice == "5":
            buy_products()

        elif choice == "6":
            print("Дякуємо за покупку!")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


# Головне меню програми
def main():
    while True:
        print("\n==============================")
        print("       МІНІ МАГАЗИН")
        print("==============================")
        print("1. Увійти як покупець")
        print("2. Увійти як адміністратор")
        print("3. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            customer_menu()

        elif choice == "2":
            admin_login()

        elif choice == "3":
            print("Програму завершено.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


# Запуск програми
main()