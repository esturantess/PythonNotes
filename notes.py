from datetime import date
from datetime import datetime
import os
from os import listdir


class NewEx(Exception):
    pass


class RepetitionEx(Exception):
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
            elif user_command == "del":
                note_name = input("Введите название заметки: ")
                os.remove(note_name + ".txt")
                print("Заметка удалена.")
            elif user_command == "read":
                file_name = input("Введите название заметки: ")
                if (file_name + ".txt") in note_list:
                    with open(file_name + ".txt") as current_note:
                        for line in current_note:
                            print(line)
            elif user_command == "list":
                if len(note_list) == 0:
                    print("Заметок пока нет.")
                else:
                    print(note_list)
            elif user_command == "date":
                note_year = input("Введите год: ")
                note_month = input("Введите месяц: ")
                note_day = input("Введите день: ")
                for file in note_list:
                    with open (file) as current_file:
                        note_date = current_file.readlines()
                        print(note_date)
            elif user_command == "stop":
                cycle_status = False

        else:
            raise NewEx()
    except NewEx:
        print("Неверная команда, попробуйте еще раз!")
    except RepetitionEx:
        print("Заметка с таким названием уже существует.")
