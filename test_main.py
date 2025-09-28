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
        assert len(book.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    def test_add_new_book_neggative_add_same_book(self, book):

        book.add_new_book('Марсианин')
        book.add_new_book('Марсианин')

        assert len(book.books_genre) == 1


    @pytest.mark.parametrize(
        'name_of_book',            
        [
        '',
        'Келлская книга:тайны древних манускриптов',
        'Четыреста пятьдесят один градус по Фаренгейту'
        ]
    )
    def test_add_new_book_neggative_add_book_name_out_of_range(self, book, name_of_book):

        book.add_new_book(name_of_book)

        assert len(book.books_genre) == 0        

    def test_add_new_book_add_book_without_genre(self, book):

        book.add_new_book('Марсианин')

        assert  book.books_genre['Марсианин'] == ''          

    def test_set_book_genre_add_genre(self, book):

        book.books_genre['Марсианин']=''
        book.set_book_genre('Марсианин','Фантастика')

        assert  book.books_genre['Марсианин'] == 'Фантастика'          

    def test_set_book_genre_neggative_add_genre_for_unknown_book(self, book):

        book.set_book_genre('Марсианин','Боевик')

        assert  len(book.books_genre) == 0  

    def test_set_book_genre_neggative_add_unknown_genre(self, book):

        book.books_genre['Марсианин']=''
        book.set_book_genre('Марсианин','Боевик')

        assert  book.books_genre['Марсианин'] == ''     

    def test_get_book_genre_get_genre(self, book):

        book.books_genre['Марсианин']='Фантастика'

        assert book.get_book_genre('Марсианин') == 'Фантастика'

    def test_get_books_with_specific_genre_get_books_fantastic(self, book):

        dict_of_books={'Марсианин':'Фантастика', 'Тачки':'Мультфильмы', 'Проект Аве Мария':'Фантастика'}
        book.books_genre.update(dict_of_books)
        list_of_book=book.get_books_with_specific_genre('Фантастика')
        
        assert (len(list_of_book)==2) and ('Марсианин' in list_of_book) and ('Проект Аве Мария' in list_of_book)

    def test_get_books_genre_get_list_of_books(self, book):

        dict_of_books={'Марсианин':'Фантастика', 'Тачки':'Мультфильмы', 'Проект Аве Мария':'Фантастика'}
        book.books_genre.update(dict_of_books)
        list_of_book=book.get_books_genre()

        assert (len(list_of_book) == 3) and (list_of_book['Марсианин']=='Фантастика') and (list_of_book['Тачки']=='Мультфильмы') and (list_of_book['Проект Аве Мария']=='Фантастика')

    def test_get_books_for_children_get_book_without_adult_genre(self, book):

        dict_of_books={'Марсианин':'Фантастика', 'Десять негритят':'Детективы', 'Оно':'Ужасы'}
        book.books_genre.update(dict_of_books)

        assert (len(book.get_books_for_children()) == 1) and ('Марсианин' in book.get_books_for_children())

    def test_add_book_in_favorites_add_two_books(self, book):

        dict_of_books={'Марсианин':'Фантастика', 'Тачки':'Мультфильмы', 'Проект Аве Мария':'Фантастика'}
        book.books_genre.update(dict_of_books)
        book.add_book_in_favorites('Марсианин')
        book.add_book_in_favorites('Проект Аве Мария')


        assert len(book.favorites) == 2

    def test_add_book_in_favorites_neggative_add_unknowbook_in_favourites(self, book):

        book.add_book_in_favorites('Мечтают ли андроиды об электроовцах')

        assert len(book.favorites) == 0

    def test_add_book_in_favorites_neggative_add_same_book_in_favourites(self, book):

        dict_of_books={'Марсианин':'Фантастика', 'Тачки':'Мультфильмы', 'Проект Аве Мария':'Фантастика'}
        book.books_genre.update(dict_of_books)
        book.add_book_in_favorites('Марсианин')
        book.add_book_in_favorites('Марсианин')

        assert len(book.favorites) == 1

    def test_delete_book_from_favorites_delete_one_book(self, book):

        book.favorites=['Проект Аве Мария','Марсианин']
        book.delete_book_from_favorites('Проект Аве Мария')

        assert (len(book.favorites) == 1) and ('Марсианин' in book.favorites)

    def test_get_list_of_favorites_books_get_list_of_favorites_books(self, book):

        book.favorites=['Проект Аве Мария','Марсианин']

        assert (len(book.get_list_of_favorites_books()) == 2) and ('Марсианин' in book.get_list_of_favorites_books()) and ('Проект Аве Мария' in book.get_list_of_favorites_books())


