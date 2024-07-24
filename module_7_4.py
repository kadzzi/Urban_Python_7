team1_num, team2_num = 5, 6
print('В команде Мастера кода участников: %s !' % team1_num)
print('Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num))

score_1, score_2 = 40, 42
team1_time = 18015.2357
team2_time = 17873.8229
decimal_n = 1  # Число заков после запятой

print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Волшебники данных решили задачи за {:.2f} с !'.format(team1_time))
print('Волшебники данных решили задачи за {0:.{1}f} с !'.format(team1_time, decimal_n))
print('Волшебники данных решили задачи за {number:.{digits}f} с !'.format(number=team1_time, digits=decimal_n))
print('Волшебники потратили {0:.{2}f} с, а Мастера - {1:.{2}f} с !'.format(team1_time, team2_time, decimal_n))

challenge_result = 'Мастера кода'
tasks_total = score_1 + score_2
time_avg = round(sum([team1_time, team2_time]) / sum([score_1, score_2]), decimal_n)

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: победа команды {challenge_result}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
