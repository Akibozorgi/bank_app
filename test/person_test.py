from datetime import date

from controller.person_controller import PersonController
from model.person import Person
from repository.person_repository import PersonRepository
from validation.validator import person_validator

# id = int(input("Enter ID : "))
# name = input("Enter Name : ")
# family = input("Enter Family : ")
# birth_date = input("Enter Birth Date : ")
# person = Person(id, name, family, birth_date)

person_controller = PersonController()
print(person_controller.save("Omid11", "Safaii", date(2000, 1, 1), "om_s", "omid123"))

# repo = PersonRepository()
# person = Person(100, 'ahmadreza', 'mohseni', '2010-7-29','ali', 'ali123')

# Test Passed
# repo.save(person)

# Test Passed
# print(person_validator(person))
# repo.edit(person)

# Test Passed
# repo.remove(100)

# Test Passed
# print(repo.find_all())

# Test Passed
# print(repo.find_by_id(239))

# Test Passed
# print(repo.find_by_name_and_family('C', 'G'))