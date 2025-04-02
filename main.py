from view.person_view import PersonView
from view.card_view import CardView
from view.transaction_view import TransactionView
from repository.database_maker import create_database
create_database()


#ui = PersonView()
ui= CardView()
#ui= TransactionView()
