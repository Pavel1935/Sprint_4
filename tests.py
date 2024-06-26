from main import BooksCollector

class TestBooksCollector:
    import pytest


    def test_add_new_book_good_name_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Как убивали Спартак')
        assert collector.books_genre['Как убивали Спартак'] == ''

    def test_length_of_book_more_40_not_in_collection(self):
        collector = BooksCollector()
        collector.add_new_book("Как убивали убивают и будут убивать Спартак")
        assert "Как убивали убивают и будут убивать Спартак" not in collector.books_genre

    def test_add_new_book_set_book_genre_book_in_ganer_OK(self):
        collector = BooksCollector()
        collector.add_new_book('Как убивали Спартак')
        collector.set_book_genre('Как убивали Спартак', 'Фантастика')
        assert collector.books_genre['Как убивали Спартак'] == 'Фантастика'

    def test_set_book_genre_no_book_dont_have(self):
        collector = BooksCollector()
        collector.add_new_book('Как убивали Спартак')
        collector.set_book_genre('Что то там про 300', 'Фантастика')
        assert collector.books_genre['Как убивали Спартак'] != 'Фантастика'

    @pytest.mark.parametrize('book_name, genre',
                             [['Как убивали Спартак', 'Фантастика'], ['Спартак Чемпион', 'Ужасы']])
    def test_get_books_with_specific_genre_ok(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_with_specific_genre(genre) == [book_name]

    @pytest.mark.parametrize('book_name, genre',
                             [['Как убивали Спартак', 'Ужасы'], ['гинер все купил', 'Детективы']])
    def test_get_books_genre_two_books_ok(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_genre() == {book_name: genre}

    def test_set_book_genre_no_name_dont_have_in_genre(self):
        collector = BooksCollector()
        initial_count = len(collector.books_genre)
        collector.add_new_book('')
        collector.set_book_genre('', 'Фантастика')
        assert len(collector.books_genre) == initial_count
        for name, genre in collector.books_genre.items():
            assert genre != 'Фантастика'

    @pytest.mark.parametrize(
        "books, expected",
        [
            ([('Книга_one', 'Фантастика'), ('Книга_two', 'Мультфильмы')], ['Книга_one', 'Книга_two'])])
    def test_get_books_for_children_expected_children(self, books, expected):
        collector = BooksCollector()
        for book, genre in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        result = collector.get_books_for_children()
        assert result == expected

    def test_add_book_in_favorites_new_books_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Как убивали Спартак')
        collector.add_book_in_favorites('Как убивали Спартак')
        assert 'Как убивали Спартак' in collector.favorites

    def test_delete_book_from_favorites_remove_new_books_in_favorite(self):
        collector = BooksCollector()
        collector.add_new_book('Динамо и три тысячи')
        collector.add_book_in_favorites('Динамо и три тысячи')
        collector.delete_book_from_favorites('Динамо и три тысячи')
        assert 'Динамо и три тысячи' not in collector.favorites

    @pytest.mark.parametrize('books, genre', [('Как убивали Спартак', 'Ужасы'),
                                              ('Спартак Чемпион', 'Комедия')])
    def test_get_list_of_favorites_books_have_books(self, books, genre):
        collector = BooksCollector()
        collector.add_new_book(books)
        collector.set_book_genre(books, genre)
        collector.add_book_in_favorites(books)
        result = collector.get_list_of_favorites_books()
        assert books in result


    def test_get_book_genre_book_away_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Как убивали Спартак')
        collector.set_book_genre('Как убивали Спартак', 'Фантастика')
        assert collector.get_book_genre('Как убивали Спартак') == 'Фантастика'