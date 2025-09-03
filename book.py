class BOOK:
    def take_input(self):
        self.title = str(input("Enter book title: "))
        self.author = str(input("Enter book author: "))
        self.ISBN = int(input("Enter book ISBN: "))
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {str(self.ISBN)}")

b = BOOK()

b.take_input()
b.display_info()