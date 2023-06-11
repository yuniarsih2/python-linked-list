# Membuat program single linked list untuk mencatat nama pengunjung dqn judul buku yang dipinjam


class Node:
    def __init__(self, visitor_name, book_title):
        self.visitor_name = visitor_name
        self.book_title = book_title
        self.next = None


class Library:
    def __init__(self):
        self.head = None

    def borrow_book(self, visitor_name, book_title):
        new_borrowing = Node(visitor_name, book_title)
        if self.head is None:
            self.head = new_borrowing
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_borrowing

    def get_borrowed_books(self, visitor_name):
        borrowed_books = []
        current = self.head
        while current:
            if current.visitor_name == visitor_name:
                borrowed_books.append(current.book_title)
            current = current.next
        return borrowed_books

    def print_borrowed_books(self, visitor_name):
        borrowed_books = self.get_borrowed_books(visitor_name)
        if not borrowed_books:
            print("Pengunjung tidak memiliki buku yang dipinjam.")
        else:
            print(f"Buku yang dipinjam oleh {visitor_name}:")
            for book in borrowed_books:
                print(book)


# Contoh penggunaan program
library = Library()

# Mencatat peminjaman buku oleh pengunjung
library.borrow_book("Ahmad", "Harry Potter")
library.borrow_book("Siti", "To Kill a Mockingbird")
library.borrow_book("Ahmad", "The Great Gatsby")
library.borrow_book("Rita", "Pride and Prejudice")
library.borrow_book("Siti", "The Catcher in the Rye")

# Mencetak daftar buku yang dipinjam oleh pengunjung
library.print_borrowed_books("Ahmad")
# Output:
# Buku yang dipinjam oleh Ahmad:
# Harry Potter
# The Great Gatsby

library.print_borrowed_books("Siti")
# Output:
# Buku yang dipinjam oleh Siti:
# To Kill a Mockingbird
# The Catcher in the Rye

library.print_borrowed_books("Rita")
# Output:
# Buku yang dipinjam oleh Rita:
# Pride and Prejudice
