import re
from datetime import date, datetime
from model.transaction import Transaction


def transaction_validator(transaction):
    errors = []

    if not type(transaction.sender_id) == int or transaction.sender_id < 100 or transaction.sender_id > 999999:
        errors.append({"field": "sender_id", "message": "invalid sender_id"})


    if not type(transaction.receiver_id) == int or transaction.receiver_id < 100 or transaction.receiver_id > 999999:
        errors.append({"field": "receiver_id", "message": "invalid receiver_id"})

    if not type(transaction.t_id) == int:
        try:
            transaction.t_id = datetime.strptime(transaction.t_id, "%Y-%m-%d")
        except ValueError:
            errors.append({"field": "t_id", "message": "invalid t_id format"})
    else:
        errors.append({"field": "t_id", "message": "invalid t_id"})

    return errors