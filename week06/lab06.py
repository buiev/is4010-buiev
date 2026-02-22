__all__ = ["Book", "EBook"]


class Book:
    """Simple Book class.

    Attributes
    ----------
    title : str
    author : str
    year : int
    """

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        class Book:
            """Simple Book class.

            Attributes
            ----------
            title : str
            author : str
            year : int
            """

            def __init__(self, title, author, year):
                self.title = title
                self.author = author
                self.year = year

            def __str__(self):
                return f"{self.title} by {self.author} ({self.year})"

            def get_age(self, current_year: int = 2025):
                """Return the age of the book relative to current_year (default 2025)."""
                return current_year - self.year


        class EBook(Book):
            """EBook subclass extends Book with file_size in MB."""

            def __init__(self, title, author, year, file_size):
                super().__init__(title, author, year)
                self.file_size = file_size

            def __str__(self):
                return f"{self.title} by {self.author} ({self.year}) - {self.file_size} MB"


        if __name__ == '__main__':
            # Quick manual test when running the module directly
            b = Book("The Hobbit", "J.R.R. Tolkien", 1937)
            print(b)
            print("Age:", b.get_age())

            eb = EBook("Dune", "Frank Herbert", 1965, 5)
            print(eb)
            print("EBook Age:", eb.get_age())

