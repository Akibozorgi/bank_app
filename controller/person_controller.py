from model.person import Person
from service.person_service import PersonService
from validation.validator import person_validator


class PersonController:
    def __init__(self):
        self.service = PersonService()

    def save(self, name,family,birth_data, username, password):
        try:
            person = Person(None, name, family, birth_data, username, password)
            errors = person_validator(person)
            if errors:
                raise Exception(errors)

            self.service.save(person)
            return True, "Person Saved"
        except Exception as e:
            return False, f"Error : {e}"


    def edit(self,id, name,family,birth_data, username, password):
        try:
            person = Person(id, name, family, birth_data, username, password)
            errors = person_validator(person)
            if errors:
                raise Exception(errors)

            self.service.edit(person)
            return True, "Person Edited"
        except Exception as e:
            return False, f"Error : {e}"

    def remove(self,person_id):
        try:
            self.service.remove(person_id)
            return True, "Person Removed"
        except Exception as e:
            return False, f"Error : {e}"


    def find_all(self):
        try:
            return self.service.find_all()
        except Exception as e:
            return f"Error : {e}"