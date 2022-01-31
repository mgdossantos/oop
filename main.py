from book import Book

if __name__ == '__main__':
   book1= Book('a',174)
   #print(book1.title)
   print(book1.getTitle())
   book1.setTitle('new title')
   print(book1.getTitle())

   book2= Book('b',200)
   print(book2.getTitle())