import re
from datetime import date, datetime

from model.book import Book
from model.person import Person


def person_validator(person):
    errors = []
    if not type(person.name) == str or not re.match(r"^[a-zA-Z\s]{3,30}$", person.name):
        errors.append({"field": "name", "message": "invalid name"})

    if not type(person.family)== str or not re.match(r"^[a-zA-Z\s]{3,30}$", person.family):
        errors.append({"field": "family", "message": "invalid family"})

    if not type(person.birth_date) == date or type(person.birth_date) == str:
        try:
            person.birth_date = datetime.strptime(person.birth_date, "%Y-%m-%d")
        except:
            errors.append({"field": "birth_date", "message": "invalid birth date"})
    else:
        errors.append({"field": "birth_date", "message": "invalid birth_date"})
    return errors


def book_validator(book):
    errors = []
    if not type(book.title) == str or  not re.match(r"^[a-zA-Z\s\d]{3,30}$", book.title):
        errors.append({"field": "title", "message": "invalid title"})

    if not type(book.writer) == str or not re.match(r"^[a-zA-Z\s]{3,30}$", book.writer):
        errors.append({"field": "writer", "message": "invalid writer"})

    if not type(book.pages) == int or book.pages < 0:
        errors.append({"field": "pages", "message": "invalid pages"})
    return errors


def borrow_validator(borrow):
    errors = []

    if not type(borrow.borrow_date) == date or type(borrow.borrow_date) == str:
        try:
            borrow.borrow_date = datetime.strptime(borrow.borrow_date, "%Y-%m-%d")
        except:
            errors.append({"field": "borrow_date", "message": "invalid borrow date"})
    else:
        errors.append({"field": "borrow_date", "message": "invalid borrow date"})

    if not type(borrow.return_date) == date or type(borrow.return_date) == str:
        try:
            borrow.return_date = datetime.strptime(borrow.return_date, "%Y-%m-%d")
        except:
            errors.append({"field": "return_date", "message": "invalid return date"})
    else:
        errors.append({"field": "return_date", "message": "invalid return date"})


    if not type(borrow.person) == Person:
        errors.append({"field": "person", "message": "invalid person"})

    if not type(borrow.book) == Book:
        errors.append({"field": "book", "message": "invalid book"})