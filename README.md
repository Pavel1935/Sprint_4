# Sprint_4

1. test_add_new_book_good_name_new_book Проверяет что книга добавлена в словарь и ей присвоено пустое значение жанра
2. test_length_of_book_more_40_not_in_collection Проверяет что книга длинным названием не добавляется в коллекцию
3. test_add_new_book_set_book_genre_book_in_ganer_OK Метод проверяет что можно добавить книгу и установить для нее нужный жанр
4. test_set_book_genre_no_book_dont_have Метод проверяет что не добавленная книга не существует в коллекции. Перед установкой жанра книга, должна быть добавлена в коллекцию
5. test_get_books_with_specific_genre_ok Тестируем что после добавления книги и установки жанра метод верно возвращает книги, связанные с этим жанром
6. test_get_books_genre_two_books_ok Тест проверяет наличие кгниг с жанравми в словорях
7. test_set_book_genre_no_name_dont_have_in_genre Тут мы создаем книгу без имени и проверяем что ее нет в жанре Фантастика
8. test_get_books_for_children_expected_children Тест проверяет что книги с детскими жанрами добавляются в список детских книг
9. test_add_book_in_favorites_new_books_in_favorites Проверяем, что книга добавленая в список книг фоворитов, действительно находится там
10. test_delete_book_from_favorites_remove_new_books_in_favorite Тест проверяет, что добавленная книга в список фаворитов, а затем удаленная от туда, больше там не находится
11. test_get_list_of_favorites_books_have_books И в финалочке, мы проверяем что книги добавленные в список избранных книг, действительно находятся в этом списке
12. test_get_book_genre_book_away_genre Книга присутствует в коллекции
