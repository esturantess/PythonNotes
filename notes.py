import json
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


class NonExistenceEx(Exception):
    pass


def add_note(note_list):
    note_name = input("Введите название заметки: ") + ".json"
    if note_name in note_list:
        raise RepetitionEx()
    else:
        note_list.append(note_name)
        new_note = {}
        note_date = str(date.today())
        note_header = input("Введите заголовок заметки: ")
        note_text = input("Введите текст заметки: ")
        new_note.update({"date": note_date, "header": note_header, "text": note_text})
        with open(note_name, 'w') as f_n:
            json.dump(new_note, f_n)
        print("Заметка сохранена.\n")


def edit_note(note_list):
    file_name = input("Введите название заметки: ") + ".json"
    if file_name in note_list:
        with open(file_name, "w+") as current_note:
            new_note = {}
            note_date = str(date.today())
            new_header = input("Введите новый заголовок заметки: ")
            new_text = input("Введите новый текст заметки: ")
            new_note.update({"date": note_date, "header": new_header, "text": new_text})
            with open(file_name, 'w') as f_n:
                json.dump(new_note, f_n)
            print("Заметка изменена.\n")
    else:
        raise NonExistenceEx()


def del_note(note_list):
    note_name = input("Введите название заметки: ") + ".json"
    if note_name in note_list:
        os.remove(note_name)
        print("Заметка удалена.\n")
    else:
        raise NonExistenceEx()


def read_note(note_list):
    file_name = input("Введите название заметки: ") + ".json"
    if file_name in note_list:
        with open(file_name) as f_n:
            current_note = str(f_n.readlines())
            current_note = current_note.replace(current_note[0], "").replace("]", "").replace(current_note[-1], "")
            current_note = current_note.replace(current_note[0], "").replace("]", "").replace(current_note[-1], "")
            current_note = dict(json.loads(current_note))
            note_date = current_note.get("date")
            note_header = current_note.get("header")
            note_text = current_note.get("text")
            print("Вы просматриваете заметку: " + (file_name.replace(".json", "")) + "\n\n" + "Дата последнего изменения: " + note_date + "\n\n" + note_header + "\n\n" + note_text)
        print("\n")
    else:
        raise NonExistenceEx()


def get_notes_list(note_list):
    if len(note_list) == 0:
        print("Заметок пока нет.\n")
    else:
        print(note_list)
        print("\n")


def date_sorting(note_list):
    now = datetime.now()
    note_year = int(input("Введите год: "))
    note_year = str(note_year)
    if len(note_year) != 4 or int(note_year) > now.year:
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
    print("Заметки, сделанные " + user_date + ":")
    for file in note_list:
        with open(file) as current_file:
            note_date = str(current_file.readlines())
            note_date = note_date.replace(note_date[0], "").replace("]", "").replace(note_date[-1], "")
            note_date = note_date.replace(note_date[0], "").replace("]", "").replace(note_date[-1], "")
            note_date = dict(json.loads(note_date)).get("date")
            if user_date in note_date:
                print(file.replace(".json", ""))
                counter += 1
    if counter == 0:
        print("Не найдено заметок, сделанных в этот день.")
    print("\n")


def working_with_notes():
    notes_commands = ["add", "edit", "del", "read", "list", "date", "stop"]
    cycle_status = True

    while cycle_status:
        files = listdir(".")
        mytxt = filter(lambda x: x.endswith('.json'), files)
        note_list = list(mytxt)
        print(
            "Доступные команды: \nadd - Добавление заметки;\nedit - Редактирование заметки;\ndel - Удаление "
            "заметки;\nread - Чтение заметки;\nlist - Вывод списка заметок;\ndate - Вывод по дате; "
            "\nstop - Закончить работу с заметками;\n")
        try:
            user_command = input("Введите команду: ").lower()
            if user_command in notes_commands:
                if user_command == "add":
                    add_note(note_list)
                elif user_command == "edit":
                    edit_note(note_list)
                elif user_command == "del":
                    del_note(note_list)
                elif user_command == "read":
                    read_note(note_list)
                elif user_command == "list":
                    get_notes_list(note_list)
                elif user_command == "date":
                    date_sorting(note_list)
                elif user_command == "stop":
                    cycle_status = False
            else:
                raise NewEx()
        except NewEx:
            print("Неверная команда, попробуйте еще раз!\n")
        except RepetitionEx:
            print("Заметка с таким названием уже существует.\n")
        except IncorrectDateEx:
            print("Некорректное число!\n")
        except ValueError:
            print("Вы ввели строку вместо числа.\n")
        except NonExistenceEx:
            print("Заметка не найдена.\n")


working_with_notes()
