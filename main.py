#Главная задача:

class User:
    def __init__(self, login, password, phone, email, name, surname):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.login = login
        self.password = password

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nPhone: {self.phone}\nEmail: {self.email}\nLogin: {self.login}\nPassword: {self.password}"

user1 = User("tanjiro34", 1234, 6866812, "tanjiroo@gmail.com", "Танджиро", "Камадо")
user2 = User("inoske469", 4647, 9876362, "inoske469@gmail.com", "Иноске", "Хашибира")
user3 = User("zenicu148", 3245, 9172556, "zenicu1148@gmail.com", "Зеницу", "Агацума")

list_users = [user1, user2, user3]

def Show_User():
    global list_users
    for user in list_users:
        print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
        print(user)

def Search_User(login):
    global list_users
    for index, user in enumerate(list_users):
        if user.login == login:
            return index
    return -1

def Change_User(old_password,new_password):
    global list_users
    for user in list_users:
        if user.password == old_password:
            user.password = new_password

def Delete_User(login):
    global list_users
    for user in list_users:
        if user.login == login:
            list_users.remove(user)
            return f"Пользователь под ником {login} удален♻️"
    return f"Пользователь под ником {login} не найден❌"

def Vibor():
    while True:
        choice = input("""
         1. Показать всех пользователей👁️‍
         2. Найти пользователя по логину🔎
         3. Изменить данные пользователя🔄️
         4. Удалить пользователя♻️
         5. Выход⭐
        """)
        if choice == "1" or choice == "show":
            Show_User()
        elif choice == "2":
            login = input("Введите логин пользователя: ")
            index = Search_User(login)
            if index != -1:
                print(f"Пользователь найден✅ {list_users[index]}")
            else:
                print("Пользователь не найден❌")
        elif choice == "3":
            password = int(input("Введите текущий пароль пользователя: "))
            new_password = int(input("Введите новый пароль пользователя: "))
            Change_User(password,new_password)
            print("Пароль изменен🔄️")
            Show_User()
        elif choice == "4":
            login = input("Введите логин для удаления: ")
            print(Delete_User(login))
        else:
            break

def final():
    print("\n⭐⭐⭐⭐⭐(Конец)⭐⭐⭐⭐⭐")

Vibor()

final()
