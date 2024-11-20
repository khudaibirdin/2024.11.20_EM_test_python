import json


class JsonLibrary: 
    def GetLib(self) -> dict:
        with open(self._lib_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    
    def SaveLib(self, data):
        with open(self._lib_path, "w", encoding="utf-8") as file:
            data = json.dumps(data, indent=4, ensure_ascii=False)
            file.write(data)


class ClassLibraryOperations(JsonLibrary):
    def __init__(self, lib_path:str):
        self._lib_path = lib_path

    def AddBook(self, title:str, author:str, year:str) -> str:
        error = ""
        if title == "":
            error += "Название не указано\n"
        if author == "":
            error += "Автор не указан\n"
        if year == "":
            error += "Год не указан\n"

        if error != "":
            return error
        
        new_book = {
            "title":title, 
            "author":author, 
            "year":year,
            "status": "В наличии"
        }

        library = self.GetLib()
        new_id = library["ids"] + 1
        library["books"][new_id] = new_book
        library["ids"] = new_id
        self.SaveLib(library)
        return "Книга успешно добавлена"
        
        
    def DeleteBook(self, id:str):
        library = self.GetLib()
        if id in library["books"]:
            del library["books"][id]
            self.SaveLib(library)
            return "Книга успешно удалена"
        else:
            return "id введенной книги не существует в библиотеке"
        
    def GetBook(self, parameter:str, filter:str) -> list:
        library = self.GetLib()
        filtered_books = []
        for id, book in library.items():
            if parameter == book[filter]:
                filtered_book = {
                    "id": id,
                    "title": book["title"],
                    "author": book["author"], 
                    "year":book["year"],
                    "status": book["status"]
                }
                filtered_books.add(filtered_book)
        return filtered_books
        
    def GetAllBooks(self):
        library = self.GetLib()
        all_books = []
        for id, book in library["books"].items():
            book = {
                "id": id,
                "title": book["title"],
                "author": book["author"], 
                "year":book["year"],
                "status": book["status"]
            }
            all_books.append(book)
        return all_books


    def UpdateBook(self, id:str, new_status:str) -> str:
        library = self.GetLib()
        if id in library["books"]:
            library["books"][id]["status"] = new_status
            self.SaveLib(library)
            return f'Книга {id} приобрела статус "{new_status}"'
        else:
            return "id введенной книги не существует в библиотеке"

        
