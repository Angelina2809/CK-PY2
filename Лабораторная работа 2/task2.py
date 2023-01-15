class Book:
    def __init__(self, id: int,name: str, pages:int):
        """
        Создание и подготовка к работе объекта "Книга"
        :param id - идентификатор книги
        :param name - Название книги
        :param pages - Количество страниц в книге
        """
        if not isinstance(id, int):
            raise TypeError("Идентификатор книги должен быть типа int")
        if id <= 0:
            raise ValueError("Идентификатор книги должен быть положительным числом")
        self.id = id
        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно быть int")
        if pages < 0:
            raise ValueError("Количество страниц в книге не может быть отрицательным числом")
        self.pages = pages
        self.name=name
    def __str__(self)-> str:
        return f'Книга "{self.name}"'
    def __repr__(self):
        return f"Book(id_=1, name='test_name_1', pages=200)"
class Library:
    def __init__(self, books:list=[]):
        self.books=books.copy()
    def get_next_book_id(self):
        if self.books==[]:
            return 1
        else:
            return self.books[-1].id + 1
    def get_index_by_book_id(self,id):
        for i in self.books:
            if i.id==id:
                return self.books.index(i)
        raise ValueError("Книга с запрашиваемым id не сущестсвует")
books=[
    Book(1, "Золотая рыбка", 55),
    Book(2,"Новые истории",150),
    Book(3,"Руслан и Людмила",100)
]
library=Library(books)
print(library.get_index_by_book_id(2))