
import random

from ingredients import INGREDIENTS
from potions import POTIONS


# =========================
# НАЛАШТУВАННЯ ГРИ
# =========================

TOTAL_DAYS = 10
GOAL = 1000
POTION_SLOTS = 10
MAX_DAILY_SALES = 15
DAILY_INGREDIENT_COUNT = 25

balance = 0
current_day = 1
daily_sales = 0

available_ingredients = []
cauldron = []
inventory = []


# =========================
# БЕЗПЕЧНЕ ВВЕДЕННЯ
# =========================

def safe_int_input(prompt):
    """Безпечне введення числа за допомогою try/except."""
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("Помилка! Потрібно ввести ціле число.")
        return None


def pause():
    input("\nНатисни Enter, щоб продовжити...")


def get_ingredient_name(ingredient):
    if isinstance(ingredient, (tuple, list)):
        return ingredient[0]
    return ingredient


def get_potion_recipe(potion):
    return potion[0], potion[1], potion[2]


def find_potion_by_recipe(ingredients):
    selected = sorted(ingredients)

    for potion in POTIONS:
        name, price, recipe = get_potion_recipe(potion)

        if sorted(recipe) == selected:
            return potion

    return None


# =========================
# ПОЧАТОК ГРИ
# =========================

def get_daily_ingredients():
    global available_ingredients

    all_ingredients = [
        get_ingredient_name(item)
        for item in INGREDIENTS
    ]

    count = min(DAILY_INGREDIENT_COUNT, len(all_ingredients))
    available_ingredients = random.sample(all_ingredients, count)


def show_intro():
    print("=" * 45)
    print("       АЛХІМІК: ОСТАННІ 10 ДНІВ")
    print("=" * 45)
    print("Ти — алхімік, який загруз у боргах.")
    print(f"За {TOTAL_DAYS} днів потрібно зібрати {GOAL} золотих.")
    print("Вари зілля, продавай їх і врятуй свою справу!")
    print("=" * 45)


def main_menu():
    while True:
        print("\n=== ГОЛОВНЕ МЕНЮ ===")
        print("1. Грати")
        print("2. Вийти")

        choice = safe_int_input("Твій вибір: ")

        if choice is None:
            continue

        if choice == 1:
            start_game()
            return
        elif choice == 2:
            print("До зустрічі, алхіміку!")
            return
        else:
            print("Такого пункту немає!")


def start_game():
    global balance, current_day, daily_sales
    global cauldron, inventory

    balance = 0
    current_day = 1
    daily_sales = 0
    cauldron = []
    inventory = []

    get_daily_ingredients()
    show_intro()
    game_loop()


# =========================
# ОСНОВНИЙ ЦИКЛ
# =========================

def game_loop():
    while current_day <= TOTAL_DAYS:
        print("\n" + "=" * 40)
        print(f"ДЕНЬ {current_day}/{TOTAL_DAYS}")
        print(f"Золото: {balance}/{GOAL}")
        print(f"Продано сьогодні: {daily_sales}/{MAX_DAILY_SALES}")
        print("=" * 40)

        print("1. Переглянути інгредієнти")
        print("2. Книга рецептів")
        print("3. Алхімічний котел")
        print("4. Інвентар")
        print("5. Продати зілля")
        print("6. Завершити день")

        choice = safe_int_input("Твій вибір: ")

        if choice is None:
            continue

        if choice == 1:
            show_available_ingredients()
        elif choice == 2:
            recipe_book()
        elif choice == 3:
            cauldron_menu()
        elif choice == 4:
            show_inventory()
        elif choice == 5:
            sell_potions()
        elif choice == 6:
            end_day()
        else:
            print("Невідомий пункт меню!")

    show_ending()


# =========================
# ІНГРЕДІЄНТИ
# =========================

def show_available_ingredients():
    print("\n=== ІНГРЕДІЄНТИ НА СЬОГОДНІ ===")

    if not available_ingredients:
        print("Інгредієнтів немає.")
    else:
        for i, ingredient in enumerate(available_ingredients, 1):
            print(f"{i}. {ingredient}")

    pause()


# =========================
# КНИГА РЕЦЕПТІВ
# =========================

def recipe_book():
    page_size = 5
    total = len(POTIONS)
    total_pages = max(1, (total + page_size - 1) // page_size)
    page = 0

    while True:
        print("\n" + "=" * 40)
        print(f"КНИГА РЕЦЕПТІВ — СТОРІНКА {page + 1}/{total_pages}")
        print("=" * 40)

        for i in range(page * page_size,
                       min((page + 1) * page_size, total)):
            name, price, recipe = get_potion_recipe(POTIONS[i])
            print(f"\n{name} — {price} золотих")
            print("Інгредієнти: " + ", ".join(recipe))

        print("\n1. Наступна сторінка")
        print("2. Попередня сторінка")
        print("3. Вийти")

        choice = safe_int_input("Твій вибір: ")

        if choice is None:
            continue

        if choice == 1:
            page = (page + 1) % total_pages
        elif choice == 2:
            page = (page - 1) % total_pages
        elif choice == 3:
            return
        else:
            print("Невідомий пункт меню!")


# =========================
# АЛХІМІЧНИЙ КОТЕЛ
# =========================

def cauldron_menu():
    while True:
        print("\n=== АЛХІМІЧНИЙ КОТЕЛ ===")

        if cauldron:
            for i, ingredient in enumerate(cauldron, 1):
                print(f"{i}. {ingredient}")
        else:
            print("Котел порожній.")

        print("\n1. Додати інгредієнт")
        print("2. Вийняти інгредієнт")
        print("3. Зварити зілля")
        print("4. Очистити котел")
        print("5. Повернутися")

        choice = safe_int_input("Твій вибір: ")

        if choice is None:
            continue

        if choice == 1:
            add_ingredient()
        elif choice == 2:
            remove_ingredient()
        elif choice == 3:
            brew_potion()
        elif choice == 4:
            clear_cauldron()
        elif choice == 5:
            return
        else:
            print("Невідомий пункт меню!")


def add_ingredient():
    if not available_ingredients:
        print("Немає доступних інгредієнтів!")
        return

    print("\nЯкий інгредієнт додати?")
    for i, ingredient in enumerate(available_ingredients, 1):
        print(f"{i}. {ingredient}")

    print("0. Скасувати")
    choice = safe_int_input("Номер інгредієнта: ")

    if choice is None or choice == 0:
        return

    index = choice - 1

    if 0 <= index < len(available_ingredients):
        ingredient = available_ingredients.pop(index)
        cauldron.append(ingredient)
        print(f"До котла додано: {ingredient}")
    else:
        print("Неправильний номер!")


def remove_ingredient():
    if not cauldron:
        print("Котел порожній!")
        return

    print("\nЯкий інгредієнт вийняти?")
    for i, ingredient in enumerate(cauldron, 1):
        print(f"{i}. {ingredient}")

    print("0. Скасувати")
    choice = safe_int_input("Номер інгредієнта: ")

    if choice is None or choice == 0:
        return

    index = choice - 1

    if 0 <= index < len(cauldron):
        ingredient = cauldron.pop(index)
        available_ingredients.append(ingredient)
        print(f"{ingredient} повернуто до доступних інгредієнтів.")
    else:
        print("Неправильний номер!")


def brew_potion():
    if not cauldron:
        print("Спочатку додай інгредієнти!")
        return

    if len(inventory) >= POTION_SLOTS:
        print("Інвентар заповнений! Спочатку продай зілля.")
        return

    potion = find_potion_by_recipe(cauldron)

    if potion is None:
        print("Нічого не вийшло! Рецепт неправильний.")
        print("Інгредієнти залишилися в котлі.")
        return

    name, price, recipe = get_potion_recipe(potion)
    inventory.append(potion)
    cauldron.clear()

    print(f"\n✨ Ти зварив зілля «{name}»!")
    print(f"Його ціна: {price} золотих.")


def clear_cauldron():
    if not cauldron:
        print("Котел уже порожній!")
        return

    available_ingredients.extend(cauldron)
    cauldron.clear()
    print("Котел очищено. Інгредієнти повернуто.")


# =========================
# ІНВЕНТАР
# =========================

def show_inventory():
    print("\n=== ІНВЕНТАР ===")

    print("\n--- Доступні інгредієнти ---")
    if available_ingredients:
        for i, ingredient in enumerate(available_ingredients, 1):
            print(f"{i}. {ingredient}")
    else:
        print("Немає інгредієнтів.")

    print("\n--- Інгредієнти в котлі ---")
    if cauldron:
        for i, ingredient in enumerate(cauldron, 1):
            print(f"{i}. {ingredient}")
    else:
        print("Котел порожній.")

    print(f"\n--- Зілля: {len(inventory)}/{POTION_SLOTS} ---")
    if inventory:
        for i, potion in enumerate(inventory, 1):
            name, price, recipe = get_potion_recipe(potion)
            print(f"{i}. {name} — {price} золотих")
    else:
        print("Зіль поки немає.")

    print(f"\nБаланс: {balance} золотих")
    pause()


# =========================
# ПРОДАЖ ЗІЛЬ
# =========================

def sell_potions():
    global balance, daily_sales

    if not inventory:
        print("У тебе немає зіль на продаж!")
        return

    remaining = MAX_DAILY_SALES - daily_sales

    if remaining <= 0:
        print("Ліміт продажу на сьогодні вичерпано!")
        return

    print("\n=== ПРОДАЖ ЗІЛЬ ===")
    print(f"Залишилося продати сьогодні: {remaining}")

    for i, potion in enumerate(inventory, 1):
        name, price, recipe = get_potion_recipe(potion)
        print(f"{i}. {name} — {price} золотих")

    print("0. Скасувати")
    print("1. Продати всі доступні зілля")
    print("2. Вибрати зілля")

    choice = safe_int_input("Твій вибір: ")

    if choice is None or choice == 0:
        return

    if choice == 1:
        count = min(len(inventory), remaining)
        sold = inventory[:count]
        del inventory[:count]

        total = 0

        for potion in sold:
            name, price, recipe = get_potion_recipe(potion)
            total += price
            print(f"Продано «{name}» за {price} золотих.")

        balance += total
        daily_sales += count

        print(f"Зароблено: {total} золотих.")
        print(f"Баланс: {balance} золотих.")

        if inventory:
            print(f"Залишилося зіль: {len(inventory)}")

    elif choice == 2:
        sell_selected_potions(remaining)
    else:
        print("Невідомий пункт меню!")


def sell_selected_potions(remaining):
    global balance, daily_sales

    sold_count = 0

    while inventory and sold_count < remaining:
        print("\nЗілля в інвентарі:")

        for i, potion in enumerate(inventory, 1):
            name, price, recipe = get_potion_recipe(potion)
            print(f"{i}. {name} — {price} золотих")

        print("0. Завершити продаж")

        choice = safe_int_input("Номер зілля для продажу: ")

        if choice is None:
            continue

        if choice == 0:
            break

        index = choice - 1

        if 0 <= index < len(inventory):
            potion = inventory.pop(index)
            name, price, recipe = get_potion_recipe(potion)

            balance += price
            daily_sales += 1
            sold_count += 1

            print(f"Продано «{name}» за {price} золотих.")
            print(f"Баланс: {balance} золотих.")
        else:
            print("Неправильний номер!")

    print(f"Продаж завершено: {daily_sales}/{MAX_DAILY_SALES} зіль сьогодні.")


# =========================
# ЗАВЕРШЕННЯ ДНЯ
# =========================

def end_day():
    global current_day, daily_sales

    print(f"\nДень {current_day} завершено.")

    if current_day >= TOTAL_DAYS:
        current_day = TOTAL_DAYS + 1
        return

    current_day += 1
    daily_sales = 0
    get_daily_ingredients()

    print(f"Настав день {current_day}!")
    print("На ринку з'явилися нові інгредієнти.")


# =========================
# КІНЦІВКИ
# =========================

def show_ending():
    print("\n" + "=" * 45)
    print("                  КІНЕЦЬ ГРИ")
    print("=" * 45)
    print(f"Фінальний баланс: {balance} золотих")
    print(f"Необхідна сума: {GOAL} золотих")

    if balance == 0:
        print("\n=== СЕКРЕТНА КІНЦІВКА ===")
        print("Ти просто сидів 10 днів і дивився в стіну.")
        print("Кредитор: Ти шо дибіл?")
        print("Алхімік року. Безперечно.")

    elif balance >= GOAL:
        print("\n=== КІНЦІВКА: УСПІХ ===")
        print("Ти зібрав необхідну суму!")
        print("Борг сплачено, і ти можеш відкрити власну крамницю.")

    else:
        print("\n=== КІНЦІВКА: НЕВДАЧА ===")
        print("Десять днів минули, але потрібної суми немає.")
        print("Твоя алхімічна пригода завершилася невдачею.")

    print("\nДякую за гру!")


# =========================
# ЗАПУСК ГРИ
# =========================

if __name__ == "__main__":
    main_menu()
