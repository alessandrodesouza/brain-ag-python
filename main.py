from dotenv import load_dotenv
load_dotenv()

from src.infra.configure_services import register_ioc
from src.app.model.farmer.farmer import Farmer

from src.infra.db.repositories.mongo_db.mongo_db_connection import MongoDBConnection

if __name__ == '__main__':
    register_ioc()

    farmer = Farmer.create_new(document='158.397.318-46', name='John Doe')
    print(farmer)
