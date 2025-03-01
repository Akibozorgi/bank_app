from model.book import Book
from model.borrow import Borrow
from model.person import Person
from repository.person_repository import PersonRepository
from repository.book_repository import BookRepository
from repository.borrow_repository import BorrowRepository
from service.borrow_service import BorrowService
from validation.validator import person_validator, book_validator

borrow_repo = BorrowRepository()
borrow_repo.return_book(2)

# print(borrow_repo.find_non_returned_by_username("ALI"))


book1 = Book(1, "Python", "ORG", "MFT", 350)
person1 = Person(1, "Ali", "Alipour", "2000-11-11", "ali", "ali123")
borrow = Borrow(1,person1, book1)
borrow_service = BorrowService()
borrow_service.borrow_book(borrow)



# book1 = Book(1, "Python", "ORG", "MFT", 350)
# book_repo = BookRepository()
#
# errors = book_validator(book1)
# if not errors:
#     book_repo.save(book1)
# else:
#     print(errors)


# person1 = Person(1, "Ali", "Alipour", "2000-11-11", "ali", "ali123")
# person_repo = PersonRepository()
#
# errors = person_validator(person1)
# if not errors:
#     person_repo.save(person1)
# else:
#     print(errors)


# borrow = Borrow(4, person1, book1)
# borrow_repo = BorrowRepository()
# borrow_repo.save(borrow)
# borrow_repo.return_book(borrow)
