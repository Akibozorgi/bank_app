from datetime import date
from controller.transaction_controller import TransactionController
from model.transaction import Transaction
from repository.transaction_repository import TransactionRepository
from validation.transaction_validator import transaction_validator


# id = int(input("Enter ID : "))
# amount = int(input("Enter Amount : "))
# date_time = input("Enter Date_time : ")
# sender = input("Enter Sender : ")
# receiver = input("Enter Receiver")
# transaction = Transaction(id, amount,date_time,sender,receiver)

transaction_controller = TransactionController()
print(transaction_controller.save("Omid11", "Safaii", date(2000, 1, 1), "om_s", "omid123"))

# repo = TransactionRepository()
# transaction = transaction(100, 'ahmadreza', 'mohseni', '2010-7-29','ali', 'ali123')

# Test Passed
# repo.save(transaction)

# Test Passed
# print(transaction_validator(person))
# repo.edit(transaction)

# Test Passed
# repo.remove(100)

# Test Passed
# print(repo.find_all())

# Test Passed
# print(repo.find_by_id(239))

# Test Passed
# print(repo.find_by_name_and_family('C', 'G'))