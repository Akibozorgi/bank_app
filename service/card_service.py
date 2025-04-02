
from model.card import Card
from repository.card_repository import CardRepository

class CardService:
    def __init__(self):
        self.repo = CardRepository()

    def save(self, card):
        self.repo.save(card)

    def edit(self,card):
        self.repo.edit(card)

    def remove(self, card_id):
        self.repo.remove(card_id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self, card_id):
        return self.repo.find_by_id(card_id)

    def find_by_bank_name_and_card_number(self, bank_name, card_number):
        return self.repo.find_by_bank_name_and_card_number(bank_name, card_number)

    def find_by_username_and_password(self, username, password):
        return self.repo.find_by_username_and_password(username, password)