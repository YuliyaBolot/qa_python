# qa_python
Юнит-тесты:

Тест №1 test_fillings_dictionary_true: Проверка корректного заполнения 
словаря books_genre = {ключ:
значение}.

Тест №2 test_add_new_book_do_not_add_books: Негативный сценарий. Книги 
без названия и с названием более
40 символов - не попадают в словарь books_genre.

Тест №3 test_add_new_book_try_add_existed_book: Негативный сценарий. 
Попытка добавить в словарь books_genre
книгу, которая уже есть в словаре.

Тест №4 test_set_book_genre: Проверка присвоения жанра книге.      

Тест №5 test_set_book_genre_try_to_set_genre_which_not_in_genre_list: 
Негативный сценарий. Попытка установить книге жанр, которого нет
в списке genre.

Тест №6 test_get_books_with_specific_genre_add_book_to_list: Проверка 
добавления книг определенного жанра в список
books_with_specific_genre.

Тест №7 test_get_books_for_children_add_child_book: Проверка добавления 
книг в список для детей в соответствии с
жанром книги.

Тест №8 test_add_book_in_favorites_add_two_favourite_book: Проверка 
добавления книг из словаря books_genre в список
избранных.

Тест №9 test_add_book_in_favorites_try_to_add_repeat_book: Негативный 
сценарий. Попытка добавить в избранный список книгу,
которая уже есть в этом списке.

Тест №10 
test_add_book_in_favorites_try_to_add_book_which_not_in_dictionary: 
Негативный сценарий. Попытка добавить в избранный список книгу, которая 
отсутствует в словаре books_genre.

Тест №11 test_delete_book_from_favorites_list: Проверка удаления книги из 
избранного списка.


 
