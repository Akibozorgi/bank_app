import mysql.connector
from model.transaction import Transaction

class TransactionRepository:
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

    def save(self, transaction):
        self.connect()
        self.cursor.execute(
            "INSERT INTO transactions (t_id, AMOUNT,DATE_TIME,sender_id, receiver_id) VALUES (%s,%s,%s,%s,%s)",
            [transaction.p_id, transaction.amount,transaction.date_time, transaction.sender, transaction.receiver]
        )
        self.connection.commit()
        self.disconnect()


    def edit(self, transaction):
        self.connect()
        self.cursor.execute(
            "UPDATE transactions SET transactions.t_id=%s, AMOUNT=%s, DATE_TIME=%s, SENDER_ID=%s,receiver_id=%s WHERE transactions.T_ID=%s",
            [transaction.p_id, transaction.amount, transaction.date_time, transaction.sender, transaction.reciver,transaction.p_id]
        )
        self.connection.commit()
        self.disconnect()

    def remove(self, person_id):
        self.connect()
        self.cursor.execute("DELETE FROM transactions WHERE T_ID=%s", [person_id])
        self.connection.commit()
        self.disconnect()
#transaction_list = list(map(lambda p: Transaction(*p), self.cursor.fetchall()))
    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM transactions ORDER BY sender_id, receiver_id")
        transaction_list = list(map( lambda p:Transaction(*p), self.cursor.fetchall()))
        self.disconnect()
        return transaction_list

    def find_by_id(self, person_id):
        self.connect()
        self.cursor.execute("SELECT * FROM transactions WHERE T_ID=%s", [person_id])
        transaction = self.cursor.fetchone()
        self.disconnect()
        return None

    def find_by_sender_id_and_receiver_id(self,  sender_id,receiver_id):
        self.connect()
        self.cursor.execute("SELECT * FROM transactions WHERE sender_id LIKE %s AND receiver_id LIKE %s", [sender_id + "%", receiver_id + "%"])
        person_list = self.cursor.fetchall()
        self.disconnect()
        return person_list



