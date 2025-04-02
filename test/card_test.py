from datetime import date

from controller.card_controller import CardController
from model.card import Card
from repository.card_repository import CardRepository
from validation import card_validator


# c_id = int(input("Enter C_ID : "))
# bank_name = input("Enter Bank_name : ")
# card_number =  int(input("Enter Card_number : "))
# expire_date = int(input("Enter Expire_date : "))
# cvv2 = int (input("Enter Cvv2 : "))
# password = int(input("Enter Password : "))
# amount = int(input("Enter amount : "))
# person = Person(c_id, bank_name,card_number,expire_date,cvv2, password,amount)

card_controller = CardController()
print(card_controller.save("Omid11", "Mellat", date(2000, 1, 1), "om_s", "omid123"))

# اطلاعات شخص
person = (1, "Omid", "Safaii", date(2000, 1, 1), "om_s", "omid123")

# اطلاعات کارت بانکی
bank_name = "Mellat"
card_number = "1234567812345678"  # شماره کارت 16 رقمی
expire_date = date(2025, 12, 31)  # تاریخ انقضا
cvv2 = "123"  # CVV2 3 رقمی
password = "password123"  # رمز عبور
amount = 5000  # موجودی کارت

# ساخت کارت بانکی جدید
card = Card(0, bank_name, card_number, expire_date, cvv2, password, amount, person)

# کنترلر کارت
card_controller = CardController()

# تست ذخیره‌سازی کارت
status, message = card_controller.save(card)

# نمایش نتیجه ذخیره‌سازی
if status:
    print("Card saved successfully!")
else:
    print(f"Failed to save card: {message}")


# repo = CardRepository()
#card = Card(100, 'ahmadreza', 'mohseni', '2010-7-29','ali', 'ali123')

# Test Passed
# repo.save(card)

# Test Passed
# print(card_validator(person))
# repo.edit(card)

# Test Passed
# repo.remove(100)

# Test Passed
# print(repo.find_all())

# Test Passed
# print(repo.find_by_id(239))

# Test Passed
# print(repo.find_by_name_card_and ('C', 'G'))