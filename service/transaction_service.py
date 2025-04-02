import mysql.connector
from model.transaction import Transaction
from repository.transaction_repository import Transaction


class TransactionService:
    def __init__(self):
        self.repo = TransactionService

    def save(self, transaction):
        self.repo.save(transaction)

    def edit(self, transaction):
        self.repo.edit(transaction)

    def remove(self, tranceaction_id):
        self.repo.remove(tranceaction_id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self, person_id):
        return self.repo.find_by_id(person_id)

    def find_by_name_and_family(self, name, family):
        return self.repo.find_by_name_and_family(name, family)

    def find_by_username_and_password(self, username, password):
        return self.repo.find_by_username_and_password(username, password)
