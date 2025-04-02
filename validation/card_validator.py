import re
from datetime import date


def card_validator(card):
    errors = []

    # بررسی نام بانک
    if not type(card.bank_name) == str or not re.match(r"^[a-zA-Z\s]{3,30}$", card.bank_name):
        errors.append({"field": "bank_name", "message": "Invalid bank name"})

    # بررسی شماره کارت
    if not type(card.card_number) == str or not re.match(r"^\d{16}$", card.card_number):
        errors.append({"field": "card_number", "message": "Invalid card number"})

    # بررسی تاریخ انقضا
    if not isinstance(card.expire_date, date):
        errors.append({"field": "expire_date", "message": "Invalid expire date"})

    # بررسی CVV2
    if not type(card.cvv2) == str or not re.match(r"^\d{3}$", card.cvv2):
        errors.append({"field": "cvv2", "message": "Invalid cvv2"})

    # بررسی رمز عبور
    if not type(card.password) == str or len(card.password) < 6:
        errors.append({"field": "password", "message": "Invalid password"})

    # بررسی مبلغ
    if not isinstance(card.amount, (int, float)) or card.amount <= 0:
        errors.append({"field": "amount", "message": "Invalid amount"})

    # بررسی شخص
    if not card.person:
        errors.append({"field": "person", "message": "Invalid person"})

        # todo : has error
        # if not type(person.birth_date) == date or type(person.birth_date) == str:
        #     try:
        #         person.birth_date = datetime.strptime(person.birth_date, "%Y-%m-%d")
        #     except:
        #         errors.append({"field": "birth_date", "message": "invalid birth date"})
        # else:
        #     errors.append({"field": "birth_date", "message": "invalid birth_date"})

    return errors