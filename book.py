class Book:

    def __init__(self, title,numberPages):
        self.title=title
        self.numberPages=numberPages

    def setTitle(self,newTitle):
        self.title=newTitle

    def getTitle(self):
        return self.title