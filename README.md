# qa_python
Методы приложения BooksCollector (main.py) покрыты 18 тестами (test_main.py), покрытие тестами составило 100%:
Name      Stmts   Miss  Cover
-----------------------------
main.py      38      0   100%
-----------------------------
TOTAL        38      0   100%

1. Метод add_new_book покрыт тестами test_add_new_book_add_two_books(проверка добавления книг), test_add_new_book_neggative_add_same_book (проверка невозможности добавление уже внесенной в словарь книги), test_add_new_book_neggative_add_book_name_out_of_range(проверка невозможности добавления книги с количеством символов в названии меньше 1 и больше 40), test_add_new_book_add_book_without_genre (проверка отсутствия жанра у добавленной книги)
2. Метод set_book_genre покрыт тестами test_set_book_genre_add_genre(проверка добавления жанра книги), test_set_book_genre_neggative_add_genre_for_unknown_book(проверка отсутствия возможности присвоения жанра книге, которая не добавлена в основной словарь), test_set_book_genre_neggative_add_unknown_genre(првоерка отсутствия возможности добавления жанра, не определенного в приложении)
3. Метод get_book_genre покрыт тестом test_get_book_genre_get_genre (проверка вывода жанра книги по ее имени)
4. Метод get_books_with_specific_genre покрыт тестом test_get_books_with_specific_genre_get_books_fantastic(проверка вывода списка всех книг с выбранным жанром)
5. Метод get_books_genre покрыт тестом test_get_books_genre_get_list_of_books(проверка вывода всего перечня книг с их жанрами)
6. Метод get_books_for_children покрыт тестом test_get_books_for_children_get_book_without_adult_genre(проверка вывода перечня книг для детей с жанром. не имеющим возрастного ограничения (ужасы и детективы))
7. Метод add_book_in_favorites покрыт тестами test_add_book_in_favorites_add_two_books(проверка добваление книг в список избранных), test_add_book_in_favorites_neggative_add_unknowbook_in_favourites(проверка невозможности добавления книги в избранное, если она отсутствует в основном словаре), test_add_book_in_favorites_neggative_add_same_book_in_favourites (проверка невозможности повторного добавления книги в список избранных)
8. Метод delete_book_from_favorites покрыт тестом test_delete_book_from_favorites_delete_one_book (проверка возможности удаления книги из перечня избранных)
9. Метод get_list_of_favorites_books покрыт тестом test_get_list_of_favorites_books_get_list_of_favorites_books(првоерка вывода перечня ниг из списка избарнных)

В каждом из тестом была применена фикстура book для создания объекта класса BooksCollector.
Параметризация была применена лишь в одно тесте test_add_new_book_neggative_add_book_name_out_of_range, так как только в нем при вводе различных данных всегда ожидался один результата. В останльных тестах в связи с уникальным ожидаемым результатом применить параметризацию было невозможно.

