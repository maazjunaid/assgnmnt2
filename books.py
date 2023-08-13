books = {'book1': { 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925 }
    , 'book2': { 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960 }
    , 'book3': { 'title': '1984', 'author': 'George Orwell', 'year': 1949 } }

books['book4'] =  {}

books['book4']['title'] = 'The Year That Rocked the World'
books['book4']['author'] = 'Mark Kurlansky'
books['book4']['year'] = 1968

print("New book added is : ",books['book4'])

print("Titles of all the books:")
for book_key, book_info in books.items():
    print(book_info['title'])

earliest_book = None
earliest_year = float('inf')  # Initialize with a high value
for book_key, book_info in books.items():
    if book_info['year'] < earliest_year:
        earliest_year = book_info['year']
        earliest_book = book_key

print("\nBook with the earliest publication year:")
print("year:", books[earliest_book]['year'])
print("Title:", books[earliest_book]['title'])
print("Author:", books[earliest_book]['author'])




