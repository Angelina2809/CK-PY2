from typing import final
class Book:
    def __init__(self, name: str, author: str):
        """
        Создание и подготовка к работе объекта "Книга"
        :param name - Название книги
        :param author - Автор книги
        """
        name: final(str) = name
        author: final(str) = author
        self.name = name
        self.author = author
    def __str__(self) -> str:
        return "Книга \"" + self.name + "\" , автор "+self.author
    def __repr__(self):
       return "Book(name=\'"+self.name+"\', author= "+ self.author+")"
class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Бумажная книга"
        :param pages - Количество страниц
        :param name - Название книги (наследованное свойство)
        :param author - Автор книги (наследованное свойство)
        """
        self.name = name
        self.author = author
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно быть int")
        if pages < 0:
            raise ValueError("Количество страниц в книге не может быть отрицательным числом")
        self.pages = pages
    def __str__(self):
        return super().__str__() + " , количество страниц " + str(self.pages)
class AudioBook(Book):
    def __init__(self, name: str, author: str,duration:float):
        self.name = name
        self.author = author
        """
        Создание и подготовка к работе объекта "Аудиокнига"
        :param duration - Продолжительность книги
        :param name - Название книги (наследованное свойство)
        :param author - Автор книги (наследованное свойство)
        """
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Продолжительность аудикниги должно быть float")
        if duration < 0:
            raise ValueError("Продолжительность аудикниги не может быть отрицательным числом")
        self.duration = duration
    def __str__(self):
        return super().__str__() + " , продолжительность " + str(self.duration)+ " минут"
book = Book("Золотая рыбка", "Пушкин")
print(book)
print(repr(book))
book1=PaperBook("Горе от ума", "Грибоедов",200)
print(book1)
book2=AudioBook("Мастер и Маргарита", "Булгаков",50.4)
print(book2)