import pytest


from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_fillings_dictionary_true(self):
        collector = BooksCollector()
        collector.add_new_book('Мор, ученик Смерти')
        assert collector.get_books_genre() == {'Мор, ученик Смерти': ''}

    @pytest.mark.parametrize('name', ['', 'Я не могу придумать книгу с таким именем!'])
    def test_add_new_book_do_not_add_books(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('name', ['Я', 'Маленькие тролли и большое наводнение..', 'Я не могу придумать книгу с таким именем'])
    def test_add_new_book_add_books_with_different_name_length(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.get_books_genre() == {name: ''}

    def test_add_new_book_try_add_existed_book(self):
        collector = BooksCollector()
        collector.books_genre = {'Мор, ученик Смерти': ''}
        collector.add_new_book('Мор, ученик Смерти')
        assert collector.get_books_genre() == {'Мор, ученик Смерти': ''}

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс','Детективы')
        assert collector.get_book_genre('Шерлок Холмс') == 'Детективы'

    def test_set_book_genre_try_to_set_genre_which_not_in_genre_list(self):
        collector = BooksCollector()
        collector.add_new_book('Запомни меня навсегда')
        collector.set_book_genre('Запомни меня навсегда','Триллер')
        assert collector.get_book_genre('Запомни меня навсегда') == ''

    def test_get_books_with_specific_genre_add_book_to_list(self):
        collector = BooksCollector()
        collector.books_genre = {'Сияние': 'Ужасы', 'Приключение Незнайки и его друзей': 'Мультфильмы', 'Чужак': 'Ужасы'}
        assert collector.get_books_with_specific_genre('Ужасы')[:] == ['Сияние', 'Чужак']

    def test_get_books_for_children_add_child_book(self):
        collector = BooksCollector()
        collector.books_genre = {'Сияние': 'Ужасы', 'Приключение Незнайки и его друзей': 'Мультфильмы',
                                 'Приключение Алисы': 'Фантастика', 'Убийство в Восточном экспрессе': 'Детективы', 'Медвежонок Паддингтон': 'Комедии' }
        assert collector.get_books_for_children()[:] == ['Приключение Незнайки и его друзей', 'Приключение Алисы', 'Медвежонок Паддингтон']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.books_genre = {'Маленький принц': 'Фантастика', 'Убийство в Восточном экспрессе': 'Детективы'}
        collector.add_book_in_favorites('Маленький принц')
        assert collector.get_list_of_favorites_books()[:] == ['Маленький принц']


    def test_add_book_in_favorites_try_to_add_repeat_book(self):
        collector = BooksCollector()
        collector.add_new_book('Маленький принц')
        collector.add_book_in_favorites('Маленький принц')
        collector.add_book_in_favorites('Маленький принц')
        assert collector.get_list_of_favorites_books()[:] == ['Маленький принц']

    def test_add_book_in_favorites_try_to_add_book_which_not_in_dictionary(self):
        collector = BooksCollector()
        collector.books_genre = {'Маленький принц': 'Фантастика', 'Убийство в Восточном экспрессе': 'Детективы'}
        collector.add_book_in_favorites('Приключение Алисы')
        assert collector.get_list_of_favorites_books()[:] == []

    def test_delete_book_from_favorites_list(self):
        collector = BooksCollector()
        collector.add_new_book('Убийство в Восточном экспрессе')
        collector.add_book_in_favorites('Убийство в Восточном экспрессе')
        collector.delete_book_from_favorites('Убийство в Восточном экспрессе')
        assert collector.get_list_of_favorites_books()[:] == []



















