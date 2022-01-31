from book import Book

if __name__ == '__main__':

    book1=Book('1984','George Orwell','294')
    print(book1.getTitle())
    book1.setTitle('1984-2')
    print(book1.getTitle())
    book2=Book('Python3 Object-Oriented Programming','Dusty Phillips','466')
    print(book2.title)
