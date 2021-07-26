class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
        pass

    def displayAvailableBooks(self):
        print("books available in the library are: ")
        for item, books in enumerate(self.books):
            print(f"\t {item+1}." + books)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"You have been issued: {bookName} book. Please keep it safe and return it within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print(f"Sorry the book {bookName} is not available or either the book is issued to the other candidate . Please Contact the Library Admistrator for more information")
            return False

    def returnBook(self, Bookname):
        if Bookname is "":
            print("Please enter the valid book name")
        else:
            self.books.append(Bookname)
            print("Thanks for returning this book hope you enjoy reading it! have a great day ahead!")


class Student:
    def requestBook(self):
        self.book = input("Enter the Book which you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the Book which you want to return: ")
        return self.book


if __name__ == "__main__":

    centralLibrary = Library(["Algorithm", "Django", "Java", "Python"])
    student= Student()
    while(True):
        welcomeMsg = '''=======WELCOME TO CENTRAL LIBRARY=========
            PLEASE CHOOSE AN OPTION.
            1.LIST ALL THE BOOKS.
            2.REQUEST A BOOK.
            3.ADD OR RETURN A BOOK.
            4.EXIT THE LIBRARY
            '''
        print(welcomeMsg)
        choice = int(input("Enter the choice: "))
        if choice == 1:
            centralLibrary.displayAvailableBooks()
        elif choice==2:
            bookName= student.requestBook()
            centralLibrary.borrowBook(bookName)
        elif choice==3:
            returnBookName= student.returnBook()
            centralLibrary.returnBook(returnBookName)
        elif choice==4:
            print("Thanks for coming to the Central Library!!!!!!!!!")
            break
        else:
            print("Invaild choice!!!!!!!!!!")
