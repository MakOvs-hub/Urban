

"Использование %"

team1_num = "В команде Мастера кода участников: %d !" % 5
team2_num = "Итого сегодня в командах участников: %d и %d !" % (5, 6)

print(team1_num)
print(team2_num)

'Использование format():'

score_2 = "Команда Волшебники данных решила задач: {} !".format(42)
team1_time = "Волшебники данных решили задачи за {} !".format(18015.2)

print(score_2)
print(team1_time)

'Использование f-строк:'
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')

challenge_result = 'победа команды Мастера кода'
tasks_total = 82
time_avg = 350.4
print(f'Результат битвы: {challenge_result}!\nПоздравляем!\n'
       f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
