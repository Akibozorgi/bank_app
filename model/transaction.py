class Transaction:
    def __init__(self,id, amount,date_time,sender,receiver):
        self.id = id
        self.amount = amount
        self.date_time = date_time
        self.sender = sender
        self.receiver = receiver

    def __repr__(self):
        return f"{self.__dict__}"