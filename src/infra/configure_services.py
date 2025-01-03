import inject
import os

# from src.domain.customer.customer_repository import CustomerRepository
# from src.infrastructure.customer.mongodb_customer_repository import MongoDBCustomerRepository
from src.infra.db.repositories.mongo_db.mongo_db_connection import MongoDBConnection

print(os.getenv('MONGO_CONNECTION_STRING'))
print(os.getenv('MONGO_DATABASE_NAME'))

connection_mongo = MongoDBConnection.create_connection(
    connection_string=os.getenv('MONGO_CONNECTION_STRING'),
    database_name=os.getenv('MONGO_DATABASE_NAME')
)

def ioc_config(binder):
    binder.bind(MongoDBConnection, connection_mongo)

def register_ioc():
    inject.configure(ioc_config)
