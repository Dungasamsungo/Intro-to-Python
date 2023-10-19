print()

with open("books.txt") as books:
    for book in books:
        clean_line = book.strip()
        print(clean_line)