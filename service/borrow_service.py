from repository.borrow_repository import BorrowRepository


class BorrowService:
    def __init__(self):
        self.repo = BorrowRepository()

    def borrow_book(self, borrow):
        previous_borrows = self.repo.find_non_returned_by_username(borrow.person.username)
        if previous_borrows:
            raise Exception('Member was already borrowed a book, and not returned')

        self.repo.borrow_book(borrow)

    def return_book(self, borrow_id):
        self.repo.return_book(borrow_id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_book_id(self, book_id):
        return self.repo.find_by_book_id(book_id)

    def find_by_username_and_title(self, username, title):
        return self.repo.find_by_username_and_title(username, title)

    def find_all_non_returned(self):
        return self.repo.find_all_non_returned()

    def find_non_returned_by_username(self, username):
        return self.repo.find_non_returned_by_username(username)
