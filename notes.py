from datetime import date
from datetime import datetime
import os
from os import listdir


class NewEx(Exception):
    pass


class RepetitionEx(Exception):
    pass


class IncorrectDateEx(Exception):
    pass


notes_commands = ["add", "edit", "del", "read", "list", "date", "stop"]
cycle_status = True

while cycle_status:
    files = listdir(".")
    mytxt = filter(lambda x: x.endswith('.txt'), files)
    note_list = list(mytxt)
    print(
        "Доступные команды: \nadd - Добавление заметки;\nedit - Редактирование заметки;\ndel - Удаление "
        "заметки;\nread - Чтение заметки;\nlist - Вывод списка заметок;\ndate - Вывод по дате;\nstop - Закончить работу с заметками;\n")
    try:
        user_command = input("Введите команду: ").lower()
        if user_command in notes_commands:
            if user_command == "add":
                note_name = input("Введите название заметки: ") + ".txt"
                if note_name in note_list:
                    raise RepetitionEx()
                else:
                    note_list.append(note_name)
                    my_file = open(note_name, "w+")
                    my_file.close()
                    with open(note_name, "w+") as new_note:
                        note_date = date.today()
                        new_note.write(str(note_date) + "\n")
                        note_header = input("Введите заголовок заметки: ")
                        new_note.write(note_header + "\n")
                        note_text = input("Введите текст заметки: ")
                        new_note.write(note_text + "\n")
                        note_id = str(datetime.now())
                        print("Заметка сохранена.\n")
            elif user_command == "edit":
                file_name = input("Введите название заметки: ") + ".txt"
                if file_name in note_list:
                    with open(file_name, "w+") as current_note:
                        note_date = date.today()
                        current_note.write(str(note_date) + "\n")
                        new_header = input("Введите новый заголовок заметки: ")
                        current_note.write(new_header + "\n")
                        new_text = input("Введите новый текст заметки: ")
                        current_note.write(new_text + "\n")
                print("\n")
            elif user_command == "del":
                note_name = input("Введите название заметки: ")
                os.remove(note_name + ".txt")
                print("Заметка удалена.\n")
            elif user_command == "read":
                file_name = input("Введите название заметки: ")
                if (file_name + ".txt") in note_list:
                    with open(file_name + ".txt") as current_note:
                        for line in current_note:
                            print(line)
            elif user_command == "list":
                if len(note_list) == 0:
                    print("Заметок пока нет.\n")
                else:
                    print(note_list)
                    print("\n")
            elif user_command == "date":
                note_year = int(input("Введите год: "))
                note_year = str(note_year)
                if len(note_year) != 4:
                    raise IncorrectDateEx()
                note_month = int(input("Введите месяц: "))
                note_month = str(note_month)
                if len(note_month) > 2 or len(note_month) < 1:
                    raise IncorrectDateEx()
                if len(note_month) == 1:
                    note_month = "0" + note_month
                note_day = int(input("Введите день: "))
                note_day = str(note_day)
                if len(note_day) > 2 or len(note_day) < 1:
                    raise IncorrectDateEx()
                if len(note_day) == 1:
                    note_day = "0" + note_day
                user_date = note_year + "-" + note_month + "-" + note_day
                counter = 0
                for file in note_list:
                    with open(file) as current_file:
                        note_date = current_file.readlines()
                        if user_date in note_date[0]:
                            print(file)
                            counter += 1
                if counter == 0: print("Не найдено заметок для даты " + user_date)
                print("\n")

            elif user_command == "stop":
                cycle_status = False
                print("\n")
        else:
            raise NewEx()
    except NewEx:
        print("Неверная команда, попробуйте еще раз!")
    except RepetitionEx:
        print("Заметка с таким названием уже существует.")
    except IncorrectDateEx:
        print("Некорректное число!")
    except ValueError:
        print("Вы ввели строку вместо числа.")
