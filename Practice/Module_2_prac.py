'''
Крестики - нолики.
'''
def check_winner():
    if area[0][0] == "X" and area[0][1] == "X" and area[0][2] == "X":
        return "X"
    if area[1][0] == "X" and area[1][1] == "X" and area[1][2] == "X":
        return "X"
    if area[2][0] == "X" and area[2][1] == "X" and area[2][2] == "X":
        return "X"
    if area[0][0] == "X" and area[1][0] == "X" and area[2][0] == "X":
        return "X"
    if area[0][1] == "X" and area[1][1] == "X" and area[2][1] == "X":
        return "X"
    if area[0][2] == "X" and area[1][2] == "X" and area[2][2] == "X":
        return "X"
    if area[0][0] == "X" and area[1][1] == "X" and area[2][2] == "X":
        return "X"
    if area[0][2] == "X" and area[1][1] == "X" and area[2][0] == "X":
        return "X"
    if area[0][0] == "0" and area[0][1] == "0" and area[0][2] == "0":
        return "0"
    if area[1][0] == "0" and area[1][1] == "0" and area[1][2] == "0":
        return "0"
    if area[2][0] == "0" and area[2][1] == "0" and area[2][2] == "0":
        return "0"
    if area[0][0] == "0" and area[1][0] == "0" and area[2][0] == "0":
        return "0"
    if area[0][1] == "0" and area[1][1] == "0" and area[2][1] == "0":
        return "0"
    if area[0][2] == "0" and area[1][2] == "0" and area[2][2] == "0":
        return "0"
    if area[0][0] == "0" and area[1][1] == "0" and area[2][2] == "0":
        return "0"
    if area[0][2] == "0" and area[1][1] == "0" and area[2][0] == "0":
        return "0"
    return '*'

def draw_area():
    for i in area:
        print(*i)# * в данном случае распечатает распакованный список
    print()

area = [["*", "*", "*"],["*", "*", "*"],["*", "*", "*"]] #создаем поле для игры
print("Добро пожаловать в крестики-нолики.")
print('-----------------------------------')
draw_area()
for turn in range(1,10):
    print(f'Ход: {turn}.')
    if turn % 2 == 0:
        turn_char = '0'
        print('Ходит игрок № 2')
    else:
        turn_char = 'X'
        print('Ходит игрок № 1')
    row = int(input("Введите номер строки (1,2,3) ")) - 1#вычитаем 1, чтобы машина корректно обработала данные (отчет с 0)
    column = int(input("Введите номер столбца (1,2,3) ")) - 1
    if area[row][column] == '*':
        area[row][column] = turn_char
    else:
        print('Ячейка уже занята, вы пропускаете ход.')
        draw_area()
        continue

    draw_area()
    if check_winner() == "X":
        print("Победил игрок № 1")
        break
    if check_winner() == "0":
        print("Победил игрок № 2")
        break
    if check_winner() == "*" and turn == 9:
        print("Ничья.")
        break