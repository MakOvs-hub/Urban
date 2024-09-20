import tkinter as tk

'Создаем back калькулятора'
def get_values():#данная функция будет запрашивать данные из окон ввода и возвращать их как результат
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, 'end')#удалит все в выбранной ячейке с и по указанный индекс.
    answer_entry.insert(0, value)#передаст по указанному адресу результат работы метода с необходимого индекса


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def dif():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)



'Создаем фронт калькулятора.'
window = tk.Tk()#Создаем окно,как экземпляр класса TK
window.title('Калькулятор')
window.geometry("200x250")
window.resizable(False,False)#Запрет на изменение размер окна

button_add = tk.Button(window, text="+", width=2,height=2, command=add)#создание функциональной кнопки на окне, command отсылка к функции
button_add.place(x=25,y=185)#размещение на окне по координатам, есть 3 метода: place,pack, grid
button_sub = tk.Button(window, text="-", width=2,height=2, command=sub)
button_sub.place(x=65,y=185)
button_div = tk.Button(window, text="/", width=2,height=2, command=dif)
button_div.place(x=105,y=185)
button_mul = tk.Button(window, text="*", width=2,height=2, command=mul)
button_mul.place(x=145,y=185)

number1_entry = tk.Entry(window,width=25)#поле для ввода
number1_entry.place(x=25, y=50)
number2_entry = tk.Entry(window,width=25)
number2_entry.place(x=25, y=100)
answer_entry = tk.Entry(window,width=25)
answer_entry.place(x=25, y=150)

number1 = tk.Label(window, text='Введите первое число: ')#Надписи согласно полям ввода
number1.place(x=25, y= 25)
number2 = tk.Label(window, text='Введите второе число: ')
number2.place(x=25, y= 75)
answer = tk.Label(window, text='Результат: ')
answer.place(x=25, y= 125)
window.mainloop()#Обновлеят информацию на окне

# данный код можно свернуть в исполняемый экзешник с помощью - pip install auto-py-to-exe
# и запустить его auto-py-to-exe