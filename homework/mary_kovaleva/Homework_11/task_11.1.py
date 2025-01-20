class Book:
    page_material = 'бумага'
    text = True

    def __init__(self, title, author, pages, isbn, is_reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_reserved = is_reserved

    def get_info(self):
        if self.is_reserved:
            return (f'Название: {self.title}, Автор: {self.author}, Страниц: {self.pages}, '
                    f'Материал: {self.page_material}, Зарезервирована')
        return (f'Название: {self.title}, Автор: {self.author}, Страниц: {self.pages}, '
                f'Материал: {self.page_material}')


class Textbook(Book):

    def __init__(self, title, author, pages, isbn, subject, school_class, is_reserved=False, tasks=True):
        super().__init__(title, author, pages, isbn, is_reserved)
        self.subject = subject
        self.school_class = school_class
        self.tasks = tasks

    def get_info(self):
        if self.is_reserved:
            return (f'Название: {self.title}, Автор: {self.author}, Страниц: {self.pages}, '
                    f'Предмет: {self.subject}, Класс: {self.school_class}, Зарезервирована')
        return (f'Название: {self.title}, Автор: {self.author}, Страниц: {self.pages}, '
                f'Предмет: {self.subject}, Класс: {self.school_class}')


books = [Book('Мартин Иден', 'Джек Лондон', 448, '978-5-17-087985-4'),
         Book('Убить пересмешника', 'Харпер Ли', 416, '978-5-17-090411-2'),
         Book('Наедине с собой', 'Марк Аврелий', 192, '978-5-17-106948-3', True),
         Book('О дивный новый мир', 'Олдос Хаксли', 352, '978-5-17-155451-4'),
         Book('Ваш покорный слуга кот', 'Сосэки Нацумэ', 576, '978-5-17-153244-4')]

for book in books:
    print(book.get_info())

textbooks = [Textbook('Математика 5 класс', 'А. Иванов', 300, '111-11',
                      'Математика', 5),
             Textbook('Английский для старших классов',
                      'И. Голубцева', 287, '23432-231', 'Английский', 11),
             Textbook('Физика 7 класс', 'В. Казанцев', 401, '3214-1234',
                      'Физика', 7, True)]

for textbook in textbooks:
    print(textbook.get_info())
