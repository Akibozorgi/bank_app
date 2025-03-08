from view.person_view import PersonView

from repository.database_maker import create_database
create_database()

ui = PersonView()


