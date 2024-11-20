from enum import Enum
import os
from classes import ClassLibraryOperations


class State(Enum):
    START = 1
    COMMAND_AWAIT = 2
    AFTER_MISTAKE = 3


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
        state = State.COMMAND_AWAIT
    
    if state == State.COMMAND_AWAIT:
        if command != None and command != "":
            try:
                command = int(command)
            except:
                print("Введена неверная команда")
                state = State.AFTER_MISTAKE
                continue
        else:
            continue
        
        if command >= 6 or command <= 0:
            print("Введите команду от 1 до 5")
            state = State.AFTER_MISTAKE
            continue

        match command:
            case 1:
                state = State.START
                continue
            
            case 2:
                state = State.START
                continue

            case 3:
                state = State.START
                continue

            case 4:
                books = lib.GetAllBooks()
                for book in books:
                    print(f"id: {book["id"]}, Название: {book["title"]}, Автор: {book["author"]}, Год издания: {book["year"]}, Статус: {book["status"]}")
                input("Нажмите Enter чтобы продолжить")
                os.system('cls')
                state = State.START
                command = ""
                continue

            case 5:
                state = State.START
                continue
    
    if state == State.AFTER_MISTAKE:
        command = input("Номер операции: ")
        state = State.COMMAND_AWAIT
    
        