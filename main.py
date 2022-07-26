help = '''
help - Напечатать справку по программе.
add - Добавить задачу в список (название задачи запрашиваем у пользователя)
show - Напечатать все добавленые задачи.'''

tasks = []

command = input('Введите команду: ')

if command == 'help':
  print(help)
elif command == 'show':
  print(tasks)
elif command == 'add':
  task = input('Введите задачу: ')
  tasks.append(task)
  print('Задача добавлена')
else:
  print('Неизвестная команда')
  
  