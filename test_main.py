import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, book):
        # создаем экземпляр (объект) класса BooksCollector

        # добавляем две книги
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(book) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    def test_add_new_book_neggative_add_same_book(self, book):

        book.add_new_book('Марсианин')
        book.add_new_book('Марсианин')

        assert len(book) == 1

    def test_add_new_book_neggative_add_book_out_of_range(self, book):

        book.add_new_book('')
        book.add_new_book('Четыреста пятьдесят один градус по Фаренгейту')

        assert len(book) == 0        