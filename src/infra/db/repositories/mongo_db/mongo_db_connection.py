from pymongo import MongoClient, ASCENDING, DESCENDING

class MongoDBConnection:
    def __init__(self, connection_string: str, database_name: str, index_definitions: dict):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self._ensure_indexes(index_definitions)

    @staticmethod
    def create_connection(connection_string: str, database_name: str):
        return MongoDBConnection(connection_string, database_name, MongoDBConnection.get_index_definitions())
    
    @staticmethod
    def get_index_definitions():
        index_definitions = {
            "farmers": [
                {"fields": [("id", ASCENDING)], "options": {"unique": True}},
                {"fields": [("name", ASCENDING)], "options": {"unique": False}},
                {"fields": [("created_at", DESCENDING)], "options": {"unique": False}},
                {"fields": [("updated_at", DESCENDING)], "options": {"unique": False}},
            ],
        }

        return index_definitions
    
    def _ensure_indexes(self, index_definitions: dict):
        for collection_name, indexes in index_definitions.items():
            collection = self.db[collection_name]
            for index in indexes:
                fields = index['fields']
                options = index.get('options', {})
                collection.create_index(fields, **options)

    def get_collection(self, collection_name: str):
        return self.db[collection_name]
