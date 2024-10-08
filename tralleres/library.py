# Clase Author
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []  # Lista para almacenar los libros escritos por el autor

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return [book.title for book in self.books]  # Devuelve una lista con los títulos de los libros

    def __str__(self):
        return f"Author: {self.name}, Books: {', '.join(self.get_books()) if self.books else 'No books yet'}"


# Clase Book
class Book:
    def __init__(self, title, pages, author):
        self.title = title
        self.pages = pages
        self.author = author
        author.add_book(self)  # Asocia el libro al autor automáticamente

    def __str__(self):
        return f"Book: {self.title}, Pages: {self.pages}, Author: {self.author.name}"


# Clase Library
class Library:
    def __init__(self):
        self.books = []  # Lista para almacenar todos los libros

    def add_book(self, book):
        self.books.append(book)

    def get_books_by_author(self, author):
        return author.get_books()  # Devuelve los libros del autor dado


# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear autores
    author1 = Author("J.K. Rowling")
    author2 = Author("J.R.R. Tolkien")

    # Crear libros y asociarlos a los autores
    book1 = Book("Harry Potter and the Philosopher's Stone", 223, author1)
    book2 = Book("Harry Potter and the Chamber of Secrets", 251, author1)
    book3 = Book("The Hobbit", 310, author2)

    # Crear biblioteca
    library = Library()

    # Agregar libros a la biblioteca
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Listar los libros de un autor en particular
    print(f"Books by {author1.name}: {library.get_books_by_author(author1)}")
    print(f"Books by {author2.name}: {library.get_books_by_author(author2)}")

    # Imprimir los detalles de los libros
    for book in library.books:
        print(book)
