
strings = ['Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!']
file_name = 'test.txt'


def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    counter = 0
    for string in strings:
        counter += 1
        strings_positions[(counter, file.tell())] = string
        file.write(f'{string}\n')
    file.close()
    return strings_positions

print(custom_write(file_name, strings))
