from abc import ABC, abstractmethod

class QueryEngine(ABC):
    @abstractmethod
    def get_table_names(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass

class SQLQueryEngine(QueryEngine):
    def __init__(self, connection,db_name):
        self.connection = connection
        self.db_name = db_name

    def get_table_names(self):
        query = "SHOW TABLES;"
        with self.connection.cursor() as cursor:
            cursor.execute(f"USE {self.db_name};")
            cursor.execute(query)
            return [table[0] for table in cursor.fetchall()]

    def execute_query(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

class MongoDBQueryEngine(QueryEngine):
    def __init__(self, connection,name):
        self.connection = connection
        self.db = self.connection[name]

    def get_table_names(self):

        return self.db.list_collection_names()

    def execute_query(self, query):
       
        pass
