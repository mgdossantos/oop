class Book:

    def __init__(self, title,author,numberPages):
        self.title=title
        self.author=author
        self.numberPages=numberPages

    def setTitle(self,newTitle):
        self.title=newTitle

    def getTitle(self):
        return self.title