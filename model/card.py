class Card:
    def __init__(self,c_id, bank_name,card_number,expire_date,cvv2, password,amount, person):
        self.c_id = c_id
        self.bank_name = bank_name
        self.card_number = card_number
        self.expire_date = expire_date
        self.cvv2 = cvv2
        self.password = password
        self.amount = amount
        self.person = person



    def __repr__(self):
        return f"{self.__dict__}"
