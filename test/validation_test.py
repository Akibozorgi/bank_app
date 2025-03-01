from model.book import Book
from model.borrow import Borrow
from model.person import Person
from validation.validator import book_validator, person_validator

book1 = Book(1, "Python", "ORG", "MFT", 350)
print(book_validator(book1))


person1 = Person(1, "Ali", "Alipour", "2000-11-11", "ali", "ali123")
print(person_validator(person1))


borrow = Borrow(1, person1, book1)
print(borrow)