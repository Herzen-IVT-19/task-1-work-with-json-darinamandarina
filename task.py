

# С помощью какой библиотеки в Python 3 можно работать с JSON файлами?

import json as j # Импортируем модуль json

# pprint позволяет в понятном для человека виде форматировать 'сложные' структуры данных 
import pprint

filename = 'data.json'

try:

    with open(filename, encoding='utf-8') as data_file:
        
        data = j.load(filename) #использовать модуль json и метод для считывания данных: (data_file)

except FileNotFoundError:

    print("Файл не найден! Файл должен называться: {}".format(filename))
    
    status = 'Файл не найден'


pprint(data)
print("Вывод .company: {}".format(data[company]))  # Вывести в форматированном виде поля: 
print("Вывод .email: {}".format(data[email])) 
print("Вывод .phone: {}".format(data[phone]))
print("Вывод .address: {}".format(data[address]))

# company, email, phone, address
