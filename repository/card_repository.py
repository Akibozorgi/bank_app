import mysql.connector
from model.card import Card


class CardRepository:
    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root123",
            database="bank_db"
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, card):
        self.connect()
        self.cursor.execute(
            "INSERT INTO Cards (c_id, bank_name,card_number,expire_date,cvv2, password,amount, person_id ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            [card.bankname, card.card_number, card.expire_date, card.cvv2, card.password, card.amount, card.person.id]
        )
        self.connection.commit()
        self.disconnect()

    def edit(self, card):
        self.connect()
        self.cursor.execute(
            "UPDATE CARDS SET c_id=%s, bank_name=%s, card_number=%s, expire_date=%s,cvv2=%s,  password=%s, person_id=%s ,amount=%s WHERE C_ID=%s",
            [card.bankname, card.card_number, card.expire_date, card.cvv2, card.password, card.amount, card.person.id]
        )
        self.connection.commit()
        self.disconnect()

    def remove(self, card_id):
        self.connect()
        self.cursor.execute("DELETE FROM PERSONS WHERE P_ID=%s", [card_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM cards ORDER BY bank_name, card_number")
        card_list = list(map(lambda c: Card(*c), self.cursor.fetchall()))
        self.disconnect()
        return card_list

    def find_by_id(self, card_id):
        self.connect()
        self.cursor.execute("SELECT * FROM cards WHERE C_ID=%s", [card_id])
        person = self.cursor.fetchone()
        self.disconnect()
        return person

    def find_by_bank_name_and_card_number(self, bank_name, card_number):
        self.connect()
        self.cursor.execute("SELECT * FROM cards WHERE bank_name LIKE %s AND card_number LIKE %s",
                            [bank_name + "%", card_number + "%"])
        card_list = self.cursor.fetchall()
        self.disconnect()
        return card_list
