from enum import Enum
import os
from classes import ClassLibraryOperations


class State(Enum):
    START = 1
    COMMAND_AWAIT = 2
    NEW_BOOK_TITLE_AWAIT = 3
    NEW_BOOK_AUTHOR_AWAIT = 4
    NEW_BOOK_YEAR_AWAIT = 5
    DELETE_BOOK_ID_AWAIT = 6
    FIND_BOOK_PARAMETER_AWAIT = 7
    UPDATING_BOOK_PARAMETER_AWAIT = 8


state = State.START
lib = ClassLibraryOperations("library.json")

print("Электронная библиотека\n")

while True:

    if state == State.START:
        print("Введите номер операции:")
        print("1 \tДобавить книгу")
        print("2 \tУдалить книгу")
        print("3 \tНайти книгу")
        print("4 \tВывести список книг")
        print("5 \tИзменить статус книги")
        command = input("Номер операции: ")
        try:
            command = int(command)
        except:
            print("Неправильно введена команда!")
            continue
        if command >= 6 or command <= 0:
            print("Неправильно введена команда!")
            continue
        else:
            match command:
                case 1:
                    state = State.NEW_BOOK_TITLE_AWAIT
                    continue
                
                case 2:
                    state = State.DELETE_BOOK_ID_AWAIT
                    continue

                case 3:
                    state = State.FIND_BOOK_PARAMETER_AWAIT
                    continue

                case 4:
                    books, _ = lib.GetAllBooks()
                    for book in books:
                        print(f"id: {book["id"]}, Название: {book["title"]}, Автор: {book["author"]}, Год издания: {book["year"]}, Статус: {book["status"]}")
                    input("Нажмите Enter чтобы продолжить")
                    os.system('cls')
                    state = State.START
                    continue

                case 5:
                    state = State.UPDATING_BOOK_PARAMETER_AWAIT
                    continue
    
    if state == State.NEW_BOOK_TITLE_AWAIT:
        new_book_title = input("Введите название книги: ")
        state = State.NEW_BOOK_AUTHOR_AWAIT
    
    if state == State.NEW_BOOK_AUTHOR_AWAIT:
        new_book_author = input("Введите автора книги: ")
        state = State.NEW_BOOK_YEAR_AWAIT
    
    if state == State.NEW_BOOK_YEAR_AWAIT:
        new_book_year = input("Введите год издания книги: ")
        result, err = lib.AddBook(new_book_title, new_book_author, new_book_year)
        if err:
            print("\nОшибка:")
            print(result)
            state = State.NEW_BOOK_TITLE_AWAIT
        else:
            print(result)
            input("Нажмите Enter чтобы продолжить")
            os.system('cls')
            state = State.START
        
    if state == State.DELETE_BOOK_ID_AWAIT:
        deleting_books_id = input("Введите id удаляемой книги: ")
        result, err = lib.DeleteBook(deleting_books_id)
        if err:
            print("\nОшибка:")
            print(result)
            continue
        else:
            print(result)
            input("Нажмите Enter чтобы продолжить")
            os.system('cls')
            state = State.START

    if state == State.FIND_BOOK_PARAMETER_AWAIT:
        parameter = input("По какому фильтру искать?\n1 \tПо названию\n2 \tПо автору\n3 \tПо году издания\nВведите номер команды: ")
        try:
            parameter = int(parameter)
        except:
            print("Неправильно введена команда!")
            continue
        if parameter >= 4 or parameter <= 0:
            print("Неправильно введена команда!")
            continue
        else:
            match parameter:
                case 1:parameter = "title"
                case 2:parameter = "author"
                case 3:parameter = "year"
            key = input("Введите запрос: ")
            if key == "":
                key = None
                print("Введен пустой запрос")
                continue
            books, err = lib.GetBook(key, parameter)
            if err:
                print("\nОшибка:")
                print(result)
                continue
            else:
                for book in books:
                    print(f"id: {book["id"]}, Название: {book["title"]}, Автор: {book["author"]}, Год издания: {book["year"]}, Статус: {book["status"]}")
                input("Нажмите Enter чтобы продолжить")
                os.system('cls')
                state = State.START
                    
    if state == State.UPDATING_BOOK_PARAMETER_AWAIT:
        updating_books_id = input("Введите id обновляемой книги: ")
        updating_books_status = input("Введите номер нового статуса книги:\n1 \tВ наличии\n2 \tВыдана\nНомер команды: ")
        try:
            updating_books_status = int(updating_books_status)
        except:
            print("Неправильно введена команда!")
            continue
        if updating_books_status >= 3 or updating_books_status <= 0:
            print("Неправильно введена команда!")
            continue
        match updating_books_status:
            case 1: updating_books_status = True
            case 2: updating_books_status = False
        result, err = lib.UpdateBook(updating_books_id, updating_books_status)
        if err:
            print("\nОшибка:")
            print(result)
            continue
        else:
            print(result)
            input("Нажмите Enter чтобы продолжить")
            os.system('cls')
            state = State.START