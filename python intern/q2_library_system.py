def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)

def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print(f"Book '{catalog[book_id][0]}' borrowed successfully.")
    elif book_id not in catalog:
        print(f"Book ID {book_id} does not exist in catalog.")
    else:
        print(f"Book '{catalog[book_id][0]}' is already borrowed.")

def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book ID {book_id} returned successfully.")
    else:
        print(f"Book ID {book_id} was not borrowed.")

def register_member(members, member_id):
    if member_id not in members:
        members.add(member_id)
        print(f"Member {member_id} registered.")
    else:
        print(f"Member {member_id} already exists. Ignoring duplicate.")

def show_available(catalog, borrowed_books):
    available = [book_id for book_id in catalog if book_id not in borrowed_books]
    if available:
        print("\nAvailable Books:")
        for book_id in available:
            title, author, year = catalog[book_id]
            print(f"  ID: {book_id}, Title: {title}, Author: {author}, Year: {year}")
    else:
        print("\nNo books available.")

def main():
    catalog = {}
    borrowed_books = []
    members = set()
    
    add_book(catalog, 101, "The Great Gatsby", "F. Scott Fitzgerald", 1925)
    add_book(catalog, 102, "To Kill a Mockingbird", "Harper Lee", 1960)
    add_book(catalog, 103, "1984", "George Orwell", 1949)
    add_book(catalog, 104, "Pride and Prejudice", "Jane Austen", 1813)
    
    register_member(members, 1001)
    register_member(members, 1002)
    register_member(members, 1003)
    register_member(members, 1002)
    
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 999)
    
    return_book(borrowed_books, 101)
    return_book(borrowed_books, 999)
    
    show_available(catalog, borrowed_books)

if __name__ == "__main__":
    main()