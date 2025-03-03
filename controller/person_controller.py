from model.person import Person
from service.person_service import PersonService
from validation.validator import person_validator


# decorator
def error_handler(my_function):
    def inner(*args, **kwargs):
        try:
            result = my_function(*args, **kwargs)
            return True, result
        except Exception as e:
            return False, e

    return inner


class PersonController:
    def __init__(self):
        self.service = PersonService()

    @error_handler
    def save(self, name, family, birth_data, username, password):
        person = Person(None, name, family, birth_data, username, password)
        errors = person_validator(person)
        if errors:
            raise Exception(errors)
        self.service.save(person)
        return "Person Saved"

    @error_handler
    def edit(self, id, name, family, birth_data, username, password):
        person = Person(id, name, family, birth_data, username, password)
        errors = person_validator(person)
        if errors:
            raise Exception(errors)
        self.service.edit(person)
        return "Person Edited"

    @error_handler
    def remove(self, person_id):
        self.service.remove(person_id)
        return "Person Removed"

    @error_handler
    def find_all(self):
        return self.service.find_all()
