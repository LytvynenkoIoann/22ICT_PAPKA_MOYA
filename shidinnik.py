user1 = {"login": "ivan", "password": "6969", "grades": [12, 10, 8, 5, 3, 7]}
user2 = {"login": "verity", "password": "heyitsme", "grades": [5, 9, 3, 7, 6, 2]}
user3 = {"login": "emilia", "password": "imsobored", "grades": [12, 11, 10, 9, 11, 10]}
user4 = {"login": "pablo", "password": "bababoy", "grades": [3, 8, 7, 12, 6, 9]}

users = [user1, user2, user3, user4]

login = input("Введіть логін: ")
password = input("Введіть пароль: ")

for user in users:
    if user["login"] == login and user["password"] == password:
        print("Вхід успішний!")
        print("Ваші оцінки:", user["grades"])

        good_grades = 0
        bad_grades = 0

        for grade in user["grades"]:
            if grade >= 5:
                good_grades += 1
            else:
                bad_grades += 1

        print("Кількість оцінок від 5 до 12:", good_grades)
        print("Кількість оцінок від 1 до 4:", bad_grades)

        break

else:print("Неправильний логін або пароль.")