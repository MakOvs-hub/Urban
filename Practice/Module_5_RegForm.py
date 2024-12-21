from random import choice


class Datadase:
    '''
        Класс базы данных, для хранения данных пользователей.
    '''

    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    '''
        Класс пользователя, содержащий атрибуты: логин, пароль.
    '''

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = Datadase() # создаем объект класса БД
    while True:
        choice  = int(input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n"))# форма с цировым вводом выбора действия
        if choice == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data: # проверяем наличие логина в нашем хранилище данных
                if password == database.data[login]: # введённый пользователем пароль совпадает с тем паролем, который хранится под ключом с логином?
                    print(f'Вход выполнен, {login}.')
                    break
                else:
                    print('Неверный пароль.')
            else:
                print('Пользователь не найден.')
        elif choice == 2:
            user = User(input("Введите логин: "),password:=input("Введите пароль: "),
                        password2:=input("Повторите пароль: ")) # создаем объект класса пользователь, моржовым оператором присваиваем значение переменным
                                                                # и запрашиваем ввод данных 3 атрибутов через input, в том числе и в переменные
            if password != password2: # завершит программу при несоответствии паролей
                print('Пароли не совпадают, попробуйте еще раз.')
                continue # завершим итерацию и запустим новую
            database.add_user(user.username, user.password) # выбираем объект БД и вызываем метод add_user, куда мы передаем введенные данные
