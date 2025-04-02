from service.transaction_service import TransactionService
from validation.transaction_validator import transaction_validator

# decorator
def error_handler(my_function):
    def inner(*args, **kwargs):
        try:
            result = my_function(*args, **kwargs)
            return True, result
        except Exception as e:
            return False, e

    return inner
#Vid, amount,date_time,sender,receiver

class TransactionController:
    def __init__(self):
        self.service = TransactionService()

    @error_handler
    def save(self, id, amount,date_time,sender,receiver):
        transaction = (None, id, amount,date_time,sender,receiver)
        errors = transaction_validator(transaction)
        if errors:
            raise Exception(errors)
        self.service.save(transaction)
        return "transaction Saved"

    @error_handler
    def edit(self, id, amount,date_time,sender,receiver):
        transaction = (id, amount,date_time,sender,receiver)
        errors = transaction_validator(transaction)
        if errors:
            raise Exception(errors)
        self.service.edit(transaction)
        return "transaction Edited"

    @error_handler
    def remove(self, sender_id):
        self.service.remove(sender_id)
        return "transaction Removed"

    @error_handler

    def find_all(self):
        return self.service.find_all()
