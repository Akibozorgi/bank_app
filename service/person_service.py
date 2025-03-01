import mysql.connector
from model.person import Person
from repository.person_repository import PersonRepository


class PersonService:
    def __init__(self):
        self.repo = PersonRepository()

    def save(self, person):
        self.repo.save(person)

    def edit(self, person):
        self.repo.edit(person)

    def remove(self, person_id):
        self.repo.remove(person_id)

    def find_all(self):
        return self.repo.find_all()

    def find_by_id(self, person_id):
        return self.repo.find_by_id(person_id)

    def find_by_name_and_family(self, name, family):
        return self.repo.find_by_name_and_family(name, family)

    def find_by_username_and_password(self, username, password):
        return self.repo.find_by_username_and_password(username, password)
