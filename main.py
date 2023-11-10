import datetime as dt

FORMAT='%d.%m.%Y %H:%M'
data = {}
#проверка на корректность данных
def check_data(data_time):
    data_time = dt.datetime.strptime(data_time, FORMAT)
    return data_time if (data_time > dt.datetime.now() and data_time != None) else False
        
#добавляем событие и автоматически ставим отмеку о том, что событие не выполнено
def add_data(data_time, new_events):
    if check_data(data_time):
        flag = False
        data[data_time] = new_events, flag
        return data
    else:
        print("Некорректно введены данные")
#просмотр всех запланированных событий    
def viewing_data(data):
    for data_t in data:
        print(f'На {data_t} запланировано {data[data_t]} событие')

def delete_data_events(data):
    data_time = input('Введите дату и время в формате: ДД:ММ:ГГ Ч:М')
    data_time = dt.datetime.strptime(data_time, FORMAT)
    if data_time in data.keys():
        del data[data_time]
    else:
        print('На эту дату у вас ничего не запланировано')
    return data
#изменение событий(без проверки отметки о выполнении)
def edit_data(data):#, new_events, flug):
    data_time = input('Введите дату и время в формате: ДД:ММ:ГГ Ч:М')
    data_time = dt.datetime.strptime(data_time, FORMAT)
    if data_time in data.keys():
        data[data_time] = input('Введите новое событие')
    else:
        print('На эту дату у вас ничего не запланировано')
    return data
    

print(add_data('26.03.2024 22:30', 'asd'))

'''
def menu():
    print('Пожалуйста, выберете действие')
    print(f'Если вы хотите добавить новую запись, введите ')
'''
