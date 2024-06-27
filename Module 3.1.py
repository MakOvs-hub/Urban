
#single_root_words_1 = ('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
#single_root_words_2 = ('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

'''Задача("Однокоренные"):
Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word,
а далее неограниченную последовательность в параметр *other_words.
Функция должна составить новый список same_words только из тех слов списка other_words,
которые содержат root_word или наоборот root_word содержит одно из этих слов.
После вернуть список same_words в качестве результата своей работы.

Пункты задачи:
Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
Создайте внутри функции пустой список same_words, который пополнится нужными словами.
При помощи цикла for переберите предполагаемо подходящие слова.
Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
После цикла верните образованный функцией список same_words.
Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей занчение.
Пример результата выполнения программы:
Исходный код:
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
Вывод на консоль:
['richiest', 'orichalcum', 'richies']
['Able', 'Disable']
Примечания:
При проверке наичлия одного слова в составе другого стоит учесть, что регистр символов не должен влять ни на что.
 ('Disablement' - 'Able') ('Able', 'able', 'AbLe' - все подходят)
В этой задаче вам могут понадобиться следующие методы строк/ключевые слова:
    а. Оператор in или count()
    b. lower()/upper().
'''

def single_root_words(root_word, *other_words):
    same_words = []  # Список для хранения слов, удовлетворяющих условию
    root_word = root_word.lower()  # Приведение корневого слова к нижнему регистру

    for word in other_words:
        word = word.lower()  # Приведение текущего слова к нижнему регистру
        if root_word in word or word in root_word:  # Проверка условия наличия в слове ключевого слова и наоборот
            same_words.append(word)

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
