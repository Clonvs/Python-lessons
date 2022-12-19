weekly_schedule = {1: 'Monday.txt', 2: 'Tuesday.txt', 3: 'Wednesday.txt',
                   4: 'Hursday.txt', 5: 'Friday.txt', 6: 'Saturday.txt', 7: 'Sunday.txt'}

team_selection = int(input('Выберите команду: 1 - добавить запись, 2 - чтение записи, 3 - изменить запись: '))
                                                            
while True:
    while team_selection < 1 or team_selection > 3: 
        team_selection = int(input('Отказано, введите команду от 1 до 3: '))  

    if team_selection == 1:
        day = int(input('Выберите день недели: '))
        note = input('Оставьте заметку: ')
        with open(weekly_schedule[day], 'a', encoding='utf-8') as f:
                f.write(note)
                f.write('\n')
        continue_or_exit = int(input('Что дальше?: 1 - выйти, 2 - продолжить: '))
        if continue_or_exit == 1:
            break
        elif continue_or_exit == 2:
            team_selection = int(input('Выберите команду: 1 - добавить запись, 2 - чтение записи, 3 - изменить запись: ')) 
        

    elif team_selection == 2:
        day = int(input('Выберите день недели: '))
        with open(weekly_schedule[day], 'r', encoding='utf-8') as f:
            print(*f.readlines())
        add = int(input("Хотите добавить запись?: 1 - да, 2 - нет: "))
        if add == 1:
            note = input('Добавьте запись: ')
            with open(weekly_schedule[day], 'a', encoding='utf-8') as f:
                f.write(note)
                f.write('\n')
            continue_or_exit = int(input('Выйти: 1 - да, 2 - нет: '))
            if continue_or_exit == 1:
                break
            else:
                team_selection = int(input('Выберите команду: 1 - добавить запись, 2 - чтение записи, 3 - изменить запись: '))  
        elif add == 2:
            continue_or_exit = int(input('Выйти: 1 - да, 2 - нет: '))
            if continue_or_exit == 1:
                break
            else:
                team_selection = int(input('Выберите команду: 1 - добавить запись, 2 - чтение записи, 3 - изменить запись: '))  


    elif team_selection == 3:
        day = int(input('Выберите день недели: '))
        note = input('Внесите изменение: ')
        with open(weekly_schedule[day], 'w', encoding='utf-8') as f:
            f.write(note)
            f.write('\n')
        continue_or_exit = int(input('Выйти: 1 - да, 2 - нет: '))
        if continue_or_exit == 1:
            break
        else:
            team_selection = int(input('Выберите команду: 1 - добавить запись, 2 - чтение записи, 3 - изменить запись: '))  