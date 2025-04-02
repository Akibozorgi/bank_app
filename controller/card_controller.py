from model.person import Person
from service.card_service import CardService
from validation.card_validator import card_validator

# decorator
def error_handler(my_function):
    def inner(*args, **kwargs):
        try:
            result = my_function(*args, **kwargs)
            return True, result
        except Exception as e:
            return False, e

    return inner


class CardController:
    def __init__(self):
        self.service = CardService()

    @error_handler
    def save(self, c_id, bank_name,card_number,expire_date,cvv2, password,amount, person):
        card = (None, c_id, bank_name,card_number,expire_date,cvv2, password,amount, person)
        errors = card_validator(card_number)
        if errors:
            raise Exception(errors)
        self.service.save(card_number)
        return "Person Saved"

    @error_handler
    def edit(self, c_id, bank_name,card_number,expire_date,cvv2, password,amount, person):
        card = (c_id, bank_name,card_number,expire_date,cvv2, password,amount, person)
        errors = card_validator(card)
        if errors:
            raise Exception(errors)
        self.service.edit(card)
        return "Card Edited"

    @error_handler
    def remove(self, c_id):
        self.service.remove(c_id)
        return "Card Removed"

    @error_handler
    def find_all(self):
        return self.service.find_all()
